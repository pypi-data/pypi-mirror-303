# breeze/models/source.py

import os
from breeze.utils.db_utils import (
    get_columns_from_database,
    get_profile,
    get_profile_name_from_dbt_project,
    get_target_from_profile,
)
from breeze.utils.yaml_utils import generate_source_yaml_content
import typer
from typing import Optional, List
from jinja2 import Template
import yaml
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedSeq


def generate_source_yml(
    schema_name: str,
    source_name: str,
    force: bool = False,
    template: Optional[str] = None,
) -> bool:
    """
    Generate or update source YAML files, using a custom template if provided.
    Returns True if the file was created or overwritten, False if it was skipped.
    """
    # Define the directory and YAML file path
    source_dir = os.path.join("models", schema_name)
    os.makedirs(source_dir, exist_ok=True)
    yml_path = os.path.join(source_dir, f"{source_name}.yml")

    # Check if the YML file already exists
    if os.path.exists(yml_path) and not force:
        typer.echo(f"✅ YML file already exists at {yml_path}. Skipping creation.")
        return False

    # Attempt to get columns by querying the database
    profile = get_profile()
    profile_name = get_profile_name_from_dbt_project()
    target = get_target_from_profile(profile, profile_name)
    database = target.get("dbname") or target.get("database")
    if not database:
        database = target.get("project")  # For BigQuery

    columns = get_columns_from_database(database, schema_name, source_name)
    if not columns:
        raise Exception(
            f"Error: Table '{source_name}' was not found in schema '{schema_name}' of database '{database}'."
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
                source_name=source_name,
                schema_name=schema_name,
                database=database,
                columns=columns_data,
            )
        except Exception as e:
            raise Exception(f"Error processing template file: {e}")
    else:
        # Proceed to generate the YAML content using default logic
        yml_data = {}
        content = generate_source_yaml_content(
            schema_name, source_name, columns, yml_data, database
        )

    # Write the content to the YML file
    with open(yml_path, "w") as yml_file:
        yml_file.write(content)

    if force and os.path.exists(yml_path):
        typer.echo(f"♻️ Source YML file at {yml_path} has been overwritten.")
    else:
        typer.echo(f"✅ Source YML file created at {yml_path}")
    return True


def add_test_to_source(
    test_names: List[str], source_name: str, columns: Optional[List[str]] = None
) -> bool:
    """
    Add one or more tests to a source YAML file.
    If columns are specified, the tests are added to those columns.
    If no columns are specified, the tests are added at the table (source) level.
    Returns True if changes were made, False otherwise.
    """
    # Initialize ruamel.yaml YAML instance
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)

    # Locate the YAML file for the source
    yml_path = find_source_yml_path(source_name)
    if not yml_path:
        raise Exception(f"YAML file for source '{source_name}' not found.")

    # Load the YAML file
    with open(yml_path, "r") as yml_file:
        yml_data = yaml.load(yml_file) or {}

    sources = yml_data.get("sources", [])
    if not sources:
        raise Exception(f"No sources found in YAML file '{yml_path}'.")

    # Find the table (source) in the YAML
    table = None
    for source in sources:
        for tbl in source.get("tables", []):
            if tbl.get("name") == source_name:
                table = tbl
                break
        if table:
            break

    if table is None:
        raise Exception(f"Source '{source_name}' not found in YAML file '{yml_path}'.")

    changes_made = False

    if columns:
        # Ensure 'columns' key exists
        if "columns" not in table or not table["columns"]:
            table["columns"] = yaml.seq()
        # Get existing columns
        existing_columns = {col["name"]: col for col in table["columns"]}
        for col_name in columns:
            if col_name not in existing_columns:
                raise Exception(
                    f"Column '{col_name}' not found in source '{source_name}'."
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
        # Add tests at table level
        tests = table.get("tests")
        if tests is None:
            table["tests"] = CommentedSeq()
            tests = table["tests"]
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


def find_source_yml_path(source_name: str) -> Optional[str]:
    """
    Find the path to the YAML file for the given source.
    """
    for root, dirs, files in os.walk("models"):
        for file in files:
            if file.endswith(".yml") or file.endswith(".yaml"):
                yml_path = os.path.join(root, file)
                with open(yml_path, "r") as yml_file:
                    yaml_loader = YAML()
                    yml_data = yaml_loader.load(yml_file)
                if yml_data and "sources" in yml_data:
                    for source in yml_data["sources"]:
                        for table in source.get("tables", []):
                            if table.get("name") == source_name:
                                return yml_path
    return None
