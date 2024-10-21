# breeze/models/model.py

import os
import json
from breeze.utils.db_utils import get_columns_from_database
from breeze.utils.yaml_utils import generate_model_yaml_content
from typing import Optional, List
from jinja2 import Template
import typer
import yaml
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedSeq


def create_empty_sql_file(
    schema_name: str,
    model_name: str,
    force: bool = False,
    template_path: Optional[str] = None,
) -> bool:
    """
    Create an SQL file for the specified model in the correct directory,
    populated with a SELECT template using ref() or a custom template.
    Returns True if the file was created or overwritten, False if it was skipped.
    """
    # Define the directory and SQL file path
    model_dir = os.path.join("models", schema_name, model_name)
    os.makedirs(model_dir, exist_ok=True)
    sql_path = os.path.join(model_dir, f"{model_name}.sql")

    # Determine the template to use
    if template_path:
        # Use the custom template provided by the user
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template file '{template_path}' not found.")
        with open(template_path, "r") as template_file:
            select_template = template_file.read()
    else:
        # Use the default template
        select_template = f"""-- {model_name}.sql

WITH 

CTE AS (
    SELECT *
    FROM {{{{ ref('model_name') }}}}
)

SELECT * FROM CTE
"""

    # Check if the SQL file already exists
    if os.path.exists(sql_path) and not force:
        typer.echo(f"✅ SQL file already exists at {sql_path}. Skipping creation.")
        return False
    else:
        # Create or overwrite the SQL file with the template
        with open(sql_path, "w") as sql_file:
            sql_file.write(select_template)
        if force and os.path.exists(sql_path):
            typer.echo(f"♻️ SQL file at {sql_path} has been overwritten.")
        else:
            typer.echo(f"📝 SQL file created at {sql_path}")
        return True


def generate_model_yml(
    model_name: str, force: bool = False, template: Optional[str] = None
) -> bool:
    """
    Generate or update model YAML files, including data_type for each column.
    Returns True if the file was created, False if it already existed.
    """
    # Locate the manifest.json file
    manifest_path = os.path.join("target", "manifest.json")

    if not os.path.exists(manifest_path):
        raise Exception(
            "manifest.json not found. Please run 'dbt compile' or 'dbt build' first."
        )

    # Load the manifest file
    with open(manifest_path, "r") as manifest_file:
        manifest = json.load(manifest_file)

    # Find the model in the manifest
    model_unique_id = None
    for node_id, node in manifest["nodes"].items():
        if node["resource_type"] == "model" and node["name"] == model_name:
            model_unique_id = node_id
            break

    if not model_unique_id:
        raise Exception(f"Model '{model_name}' not found in manifest.")

    model = manifest["nodes"][model_unique_id]

    # Extract folder_name from the model's original file path
    original_file_path = model["original_file_path"]
    # Assuming the path is something like 'models/folder_name/model_name/model_name.sql'
    path_parts = original_file_path.split(os.sep)
    try:
        folder_index = path_parts.index("models") + 1
        folder_name = path_parts[folder_index]
    except (ValueError, IndexError):
        raise Exception(f"Could not determine folder name for model '{model_name}'.")

    # Define the directory and YAML file path
    model_dir = os.path.join("models", folder_name, model_name)
    os.makedirs(model_dir, exist_ok=True)
    yml_path = os.path.join(model_dir, f"{model_name}.yml")

    # Check if the YML file already exists
    if os.path.exists(yml_path) and not force:
        typer.echo(f"✅ YML file already exists at {yml_path}. Skipping creation.")
        return False

    # Prepare columns data
    columns = get_columns_from_database(
        model["database"], model["schema"], model.get("alias") or model["name"]
    )
    if not columns:
        raise Exception(
            f"Error: Table '{model.get('alias') or model['name']}' was not found in schema '{model['schema']}' of database '{model['database']}'."
        )
    columns_data = [
        {"name": col_name, "data_type": data_type} for col_name, data_type in columns
    ]

    # Use custom template if provided
    if template:
        try:
            with open(template, "r") as template_file:
                template_content = template_file.read()
            # Create a Jinja2 template with whitespace control
            jinja_template = Template(
                template_content, trim_blocks=True, lstrip_blocks=True
            )
            # Render the template with context variables
            content = jinja_template.render(
                model_name=model_name, schema_name=model["schema"], columns=columns_data
            )
        except Exception as e:
            raise Exception(f"Error processing template file: {e}")
    else:
        # Proceed to generate the YAML content using default logic
        yml_data = {}
        content = generate_model_yaml_content(model, columns, yml_data)

    # Write content to the YML file
    with open(yml_path, "w") as yml_file:
        yml_file.write(content)

    if force and os.path.exists(yml_path):
        typer.echo(f"♻️ Model YML file at {yml_path} has been overwritten.")
    else:
        typer.echo(f"✅ Model YML file created at {yml_path}")
    return True


def add_test_to_model(
    test_names: List[str], model_name: str, columns: Optional[List[str]] = None
) -> bool:
    """
    Add one or more tests to a model YAML file.
    If columns are specified, the tests are added to those columns.
    If no columns are specified, the tests are added at the model level.
    Returns True if changes were made, False otherwise.
    """
    # Initialize ruamel.yaml YAML instance
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)

    # Locate the YAML file for the model
    yml_path = find_model_yml_path(model_name)
    if not yml_path:
        raise Exception(f"YAML file for model '{model_name}' not found.")

    # Load the YAML file
    with open(yml_path, "r") as yml_file:
        yml_data = yaml.load(yml_file) or {}

    models = yml_data.get("models", [])
    if not models:
        raise Exception(f"No models found in YAML file '{yml_path}'.")

    # Find the model in the YAML
    model = next((m for m in models if m.get("name") == model_name), None)
    if model is None:
        raise Exception(f"Model '{model_name}' not found in YAML file '{yml_path}'.")

    changes_made = False

    if columns:
        # Ensure 'columns' key exists
        if "columns" not in model or not model["columns"]:
            model["columns"] = yaml.seq()
        # Get existing columns
        existing_columns = {col["name"]: col for col in model["columns"]}
        for col_name in columns:
            if col_name not in existing_columns:
                raise Exception(
                    f"Column '{col_name}' not found in model '{model_name}'."
                )
            column = existing_columns[col_name]
            tests = column.get("tests")
            if tests is None:
                column["tests"] = CommentedSeq()
                tests = column["tests"]
            for test_name in test_names:
                if test_name not in tests:
                    tests.append(test_name)
                    changes_made = True
    else:
        # Add tests at model level
        tests = model.get("tests")
        if tests is None:
            model["tests"] = CommentedSeq()
            tests = model["tests"]
        for test_name in test_names:
            if test_name not in tests:
                tests.append(test_name)
                changes_made = True

    if changes_made:
        # Write back the YAML file
        with open(yml_path, "w") as yml_file:
            yaml.dump(yml_data, yml_file)
        return True
    else:
        return False


def find_model_yml_path(model_name: str) -> Optional[str]:
    """
    Find the path to the YAML file for the given model.
    """
    for root, dirs, files in os.walk("models"):
        for file in files:
            if file.endswith(".yml") or file.endswith(".yaml"):
                yml_path = os.path.join(root, file)
                with open(yml_path, "r") as yml_file:
                    yaml = YAML()
                    yml_data = yaml.load(yml_file)
                if yml_data and "models" in yml_data:
                    for model in yml_data["models"]:
                        if model.get("name") == model_name:
                            return yml_path
    return None
