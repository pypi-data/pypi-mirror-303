# breeze/commands/build.py

import typer
from typing import List, Optional
from breeze.models.model import create_empty_sql_file, generate_model_yml
from breeze.models.source import generate_source_yml

build_app = typer.Typer(
    help="""
Usage: breeze build [OPTIONS] COMMAND [ARGS]... 

  Build commands to generate models, YAML files, and sources.

  Use these commands to automate the creation of .sql and YAML files for dbt
  models and sources. You can use custom templates or force updates to
  existing files.

Options:
  --help  Show this message and exit.

Commands:
  model   Generate .sql files for dbt models in the specified schema.
  yml     Generate YAML files for one or more dbt models.
  source  Generate YAML files for one or more sources in a schema.
"""
)


@build_app.command()
def model(
    schema_name: str = typer.Argument(
        ..., help="The schema where the model is located."
    ),
    model_names: List[str] = typer.Argument(
        ..., help="One or more model names to generate .sql files for."
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Force overwrite existing files."
    ),
    template: Optional[str] = typer.Option(
        None, "--template", "-t", help="Path to a custom SQL template."
    ),
):
    """
    Generate SQL files for dbt models in the specified schema.

    This command will create a .sql file for each specified model in the specified schema.
    The SQL file will contain a default boilerplate with a `ref()` statement for referencing other models.

    If a file already exists, it will not be overwritten unless the `--force` option is used.

    You can use a custom template for the SQL file created by including the `--template` flag and passing the path of your template.

    Options:
      - `folder_name`: Name of the folder where the models will be created.
      - `model_names`: One or more model names for which to generate .sql files.
      - `--force`, `-f`: Overwrite existing files.
      - `--template`, `-t`: Use a custom SQL template file.

    Examples:
      - Generate .sql files for `model1` and `model2` in `my_folder`:

        \b
        breeze build model my_folder model1 model2

      - Force overwrite existing .sql file for `model1`:

        \b
        breeze build model my_schema model1 --force

      - Use a custom SQL template for `model1`:

        \b
        breeze build model my_schema model1 --template path/to/custom_template.sql
    """
    success_models = []
    skipped_models = []
    failed_models = []

    for model_name in model_names:
        try:
            file_created = create_empty_sql_file(
                schema_name, model_name, force, template
            )
            if file_created:
                success_models.append(model_name)
            else:
                skipped_models.append(model_name)
        except Exception as e:
            typer.echo(f"❌ Failed to create SQL for '{model_name}': {e}")
            failed_models.append(model_name)

    # Summary messages
    if success_models:
        typer.echo(
            f"\n📝 Successfully created SQL files for: {', '.join(success_models)}"
        )
    if skipped_models:
        typer.echo(
            f"\nSQL files skipped for: {', '.join(skipped_models)}. Use --force to overwrite."
        )
    if failed_models:
        typer.echo(f"\n❌ Failed to create SQL files for: {', '.join(failed_models)}")


@build_app.command()
def yml(
    model_names: List[str] = typer.Argument(
        ..., help="One or more model names to generate YAML files for."
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Force overwrite existing files."
    ),
    template: Optional[str] = typer.Option(
        None, "--template", "-t", help="Path to a custom YAML template."
    ),
):
    """
    Generate YAML files for one or more models.

    This command creates a YAML file for each specified model, containing metadata about the model and its columns.
    The generated YAML file will include column names, data types, and placeholders for adding tests.

    If the YAML file already exists, it will not be overwritten unless the `--force` option is used.

    You can use a custom template for the YAML file created by including the `--template` flag and passing the path of your template.

    Options:
      - `model_names`: One or more model names for which to generate YAML files.
      - `--force`, `-f`: Overwrite existing YAML files.
      - `--template`, `-t`: Use a custom YAML template file.

    Examples:
      - Generate YAML files for `model1` and `model2`:

        \b
        breeze build yml model1 model2

      - Force overwrite an existing YAML file for `model1`:

        \b
        breeze build yml model1 --force

      - Use a custom YAML template for `model1`:

        \b
        breeze build yml model1 --template path/to/custom_template.yml
    """
    success_models = []
    skipped_models = []
    failed_models = []

    for model_name in model_names:
        try:
            file_created = generate_model_yml(model_name, force, template)
            if file_created:
                success_models.append(model_name)
            else:
                skipped_models.append(model_name)
        except Exception as e:
            typer.echo(f"❌ Failed to build YAML for '{model_name}': {e}")
            failed_models.append(model_name)

    # Summary messages
    if success_models:
        typer.echo(
            f"\n✅ Successfully created YAML files for: {', '.join(success_models)}"
        )
    if skipped_models:
        typer.echo(
            f"\nYAML files skipped for: {', '.join(skipped_models)}. Use --force to overwrite."
        )
    if failed_models:
        typer.echo(f"\n❌ Failed to build YAML files for: {', '.join(failed_models)}")


@build_app.command()
def source(
    schema_name: str = typer.Argument(
        ..., help="The schema where the sources are located."
    ),
    source_names: List[str] = typer.Argument(
        ..., help="One or more source names to generate YAML files for."
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Force overwrite existing files."
    ),
    template: Optional[str] = typer.Option(
        None, "--template", "-t", help="Path to a custom YAML template."
    ),
):
    """
    Generate YAML files for one or more sources.

    This command creates a YAML file for each specified source, containing metadata about the source and its columns.
    The generated YAML file will include column names, data types, and placeholders for adding tests.

    If the YAML file already exists, it will not be overwritten unless the `--force` option is used.

    You can use a custom template for the YAML file created by including the `--template` flag and passing the path of your template.

    Options:
      - `schema_name`: Name of the schema of the sources.
      - `source_names`: One or more source names for which to generate YAML files.
      - `--force`, `-f`: Overwrite existing YAML files.
      - `--template`, `-t`: Use a custom YAML template file.

    Examples:
      - Generate YAML files for `source1` and `source2` with schema `my_schema`:

        \b
        breeze build source my_schema source1 source2

      - Force overwrite an existing YAML file for `source1`:

        \b
        breeze build source my_schema source1 -f

      - Use a custom YAML template for `source1`:

        \b
        breeze build source my_schema source1 --template path/to/source_template.yml
    """
    success_sources = []
    skipped_sources = []
    failed_sources = []

    for source_name in source_names:
        try:
            file_created = generate_source_yml(
                schema_name, source_name, force, template
            )
            if file_created:
                success_sources.append(source_name)
            else:
                skipped_sources.append(source_name)
        except Exception as e:
            typer.echo(f"❌ Failed to build YAML for source '{source_name}': {e}")
            failed_sources.append(source_name)

    # Summary messages
    if success_sources:
        typer.echo(
            f"\n✅ Successfully created YAML files for sources: {', '.join(success_sources)}"
        )
    if skipped_sources:
        typer.echo(
            f"\nYAML files skipped for sources: {', '.join(skipped_sources)}. Use --force to overwrite."
        )
    if failed_sources:
        typer.echo(
            f"\n❌ Failed to build YAML files for sources: {', '.join(failed_sources)}"
        )
