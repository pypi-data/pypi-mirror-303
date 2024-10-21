# breeze/utils/yaml_utils.py

import yaml
from typing import List, Tuple


def generate_model_yaml_content(
    model: dict, columns: List[Tuple[str, str]], existing_yml: dict
) -> str:
    model_name = model["name"]
    # Determine node_color based on model directory
    model_sql_path = model["original_file_path"]
    if "stg" in model_sql_path.lower():
        node_color = "green"
    elif "conformed" in model_sql_path.lower():
        node_color = "orange"
    elif "operational" in model_sql_path.lower():
        node_color = "red"
    else:
        node_color = "<color_id>"

    # Build the YAML content following the template
    yaml_dict = {"version": 2, "models": []}

    # Find existing model entry if any
    existing_models = existing_yml.get("models", [])
    existing_model = None

    for model_entry in existing_models:
        if model_entry.get("name") == model_name:
            existing_model = model_entry
            break

    if existing_model:
        # Use existing model data
        model_description = existing_model.get("description", "")
        if model_description == "<markdown_string>":
            model_description = ""
        model_docs = existing_model.get("docs", {})
        model_columns = existing_model.get("columns", [])
        existing_columns = {col["name"]: col for col in model_columns}
    else:
        # No existing model data
        model_description = ""
        model_docs = {}
        existing_columns = {}

    # Prepare the model dictionary
    model_dict = {
        "name": model_name,
        "tags": [],
        "description": model_description or "",
        "docs": {"show": model_docs.get("show", True), "node_color": node_color},
        "columns": [],
    }

    # Prepare columns
    for col_name, data_type in columns:
        col_entry = existing_columns.get(col_name, {})
        col_description = col_entry.get("description", "")
        if col_description == "<markdown_string>":
            col_description = ""
        column_dict = {
            "name": col_name,
            "data_type": data_type,
            "description": col_description or "",
            # Comments will be added during YAML dumping
        }
        model_dict["columns"].append(column_dict)

    yaml_dict["models"].append(model_dict)

    # Use a custom Dumper to handle comments and formatting
    yaml_content = yaml.dump(
        yaml_dict,
        sort_keys=False,
        Dumper=CustomDumper,
        width=1000,
        default_flow_style=False,
    )

    # Add comments manually
    yaml_lines = yaml_content.split("\n")
    new_yaml_lines = []
    in_columns_section = False
    columns_indent_level = None
    for i, line in enumerate(yaml_lines):
        stripped_line = line.strip()
        current_indent_level = len(line) - len(line.lstrip())
        new_yaml_lines.append(line)
        if stripped_line == "columns:":
            in_columns_section = True
            columns_indent_level = current_indent_level
        elif (
            in_columns_section
            and current_indent_level <= columns_indent_level
            and stripped_line != ""
        ):
            # We've exited the columns section
            in_columns_section = False
            columns_indent_level = None
        elif stripped_line.startswith("description:") and in_columns_section:
            # Add column-level comments
            indent = " " * (len(line) - len(line.lstrip()))
            new_yaml_lines.append(f"{indent}# tests:")
            new_yaml_lines.append(f"{indent}#   - unique")
            new_yaml_lines.append(f"{indent}#   - not_null")
    return "\n".join(new_yaml_lines)


def generate_source_yaml_content(
    schema_name: str,
    source_name: str,
    columns: List[Tuple[str, str]],
    existing_yml: dict,
    database: str,
) -> str:
    """
    Generate or update source YAML files, including data_type for each column.
    """
    # Build the YAML content following the source template
    yaml_dict = {"version": 2, "sources": []}

    # Prepare the source dictionary
    source_dict = {
        "name": schema_name.lower(),  # Using schema_name as the source name
        "database": database,
        "schema": schema_name,
        "description": "",
        "tables": [],
    }

    # Prepare the table dictionary
    table_dict = {"name": source_name, "tags": [], "description": "", "columns": []}

    # Prepare columns
    for col_name, data_type in columns:
        column_dict = {
            "name": col_name,
            "data_type": data_type,
            "description": "",
            # Comments will be added during YAML dumping
        }
        table_dict["columns"].append(column_dict)

    source_dict["tables"].append(table_dict)
    yaml_dict["sources"].append(source_dict)

    # Use a custom Dumper to handle comments and formatting
    yaml_content = yaml.dump(
        yaml_dict,
        sort_keys=False,
        Dumper=CustomDumper,
        width=1000,
        default_flow_style=False,
    )

    # Add comments manually
    yaml_lines = yaml_content.split("\n")
    new_yaml_lines = []
    in_columns_section = False
    columns_indent_level = None
    for i, line in enumerate(yaml_lines):
        stripped_line = line.strip()
        current_indent_level = len(line) - len(line.lstrip())
        new_yaml_lines.append(line)
        if stripped_line == "columns:":
            in_columns_section = True
            columns_indent_level = current_indent_level
        elif (
            in_columns_section
            and current_indent_level <= columns_indent_level
            and stripped_line != ""
        ):
            # We've exited the columns section
            in_columns_section = False
            columns_indent_level = None
        elif stripped_line.startswith("description:") and in_columns_section:
            # Add column-level comments
            indent = " " * (len(line) - len(line.lstrip()))
            new_yaml_lines.append(f"{indent}# tests:")
            new_yaml_lines.append(f"{indent}#   - unique")
            new_yaml_lines.append(f"{indent}#   - not_null")
    return "\n".join(new_yaml_lines)


# Custom YAML Dumper and representer
class CustomDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(CustomDumper, self).increase_indent(flow, False)


def str_presenter(dumper, data):
    if data == "":
        return dumper.represent_scalar("tag:yaml.org,2002:str", "", style="''")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, str_presenter, Dumper=CustomDumper)
