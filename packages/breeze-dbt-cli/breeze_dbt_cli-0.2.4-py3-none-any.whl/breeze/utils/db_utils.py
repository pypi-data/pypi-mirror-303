# breeze/utils/db_utils.py

import os
import yaml
from typing import List, Tuple

# Attempt to import database drivers
try:
    import pyodbc  # For SQL Server
except ImportError:
    pyodbc = None

try:
    import psycopg2  # For PostgreSQL and Redshift
except ImportError:
    psycopg2 = None

try:
    import snowflake.connector  # For Snowflake
except ImportError:
    snowflake = None

try:
    from google.cloud import bigquery  # For BigQuery
except ImportError:
    bigquery = None


def get_columns_from_database(
    database: str, schema: str, identifier: str
) -> List[Tuple[str, str]]:
    """
    Retrieve columns and their data types from the specified table.
    Returns a list of tuples: (column_name, data_type)
    """
    profile = get_profile()
    profile_name = get_profile_name_from_dbt_project()
    target = get_target_from_profile(profile, profile_name)
    db_type = target["type"]

    if not identifier:
        raise Exception("❌ Could not determine the table name (identifier).")

    if db_type == "postgres":
        return get_columns_postgres(target, database, schema, identifier)
    elif db_type == "redshift":
        return get_columns_redshift(target, database, schema, identifier)
    elif db_type == "snowflake":
        return get_columns_snowflake(target, database, schema, identifier)
    elif db_type == "bigquery":
        return get_columns_bigquery(target, database, schema, identifier)
    elif db_type == "sqlserver":
        return get_columns_sqlserver(target, database, schema, identifier)
    else:
        raise Exception(f"❌ Database type '{db_type}' is not supported.")


def get_target_from_profile(profile: dict, profile_name: str) -> dict:
    profile_data = profile.get(profile_name)
    if not profile_data:
        raise Exception(f"❌ Profile '{profile_name}' not found in profiles.yml.")

    # Get the target name from the profile (default to 'default' if not specified)
    target_name = profile_data.get("target", "default")

    if target_name not in profile_data["outputs"]:
        raise Exception(
            f"❌ Target '{target_name}' not found in profile '{profile_name}'."
        )

    target = profile_data["outputs"][target_name]
    return target


def get_profile_name_from_dbt_project() -> str:
    """
    Retrieve the profile name from dbt_project.yml.
    """
    dbt_project_path = os.path.join(os.getcwd(), "dbt_project.yml")
    if not os.path.exists(dbt_project_path):
        raise Exception(
            "❌ dbt_project.yml not found. Please ensure you're in a dbt project directory."
        )
    with open(dbt_project_path, "r") as dbt_project_file:
        dbt_project = yaml.safe_load(dbt_project_file)
    profile_name = dbt_project.get("profile")
    if not profile_name:
        raise Exception("❌ Profile name not found in dbt_project.yml.")
    return profile_name


def get_profile() -> dict:
    """
    Retrieve the dbt profiles.yml configuration.
    """
    home_dir = os.path.expanduser("~")
    profiles_path = os.path.join(home_dir, ".dbt", "profiles.yml")

    if not os.path.exists(profiles_path):
        raise Exception(
            "❌ profiles.yml not found. Please ensure dbt is configured correctly."
        )

    with open(profiles_path, "r") as profiles_file:
        profiles = yaml.safe_load(profiles_file)

    return profiles


def get_columns_sqlserver(
    target, database, schema, identifier
) -> List[Tuple[str, str]]:
    if pyodbc is None:
        raise Exception(
            "❌ pyodbc is not installed. Please install it with 'pip install pyodbc'."
        )

    columns = []
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={target.get('host')};"
            f"DATABASE={database};"
            f"UID={target.get('user')};"
            f"PWD={target.get('password')}"
        )
        cursor = conn.cursor()
        query = """
            SELECT COLUMN_NAME, DATA_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = ? AND TABLE_NAME = ?
            ORDER BY ORDINAL_POSITION;
        """
        cursor.execute(query, (schema, identifier))
        fetched_columns = cursor.fetchall()
        if not fetched_columns:
            raise Exception(
                f"❌ Error: Table '{identifier}' does not exist in schema '{schema}' of database '{database}'."
            )
        columns = [(row[0], row[1]) for row in fetched_columns]
        cursor.close()
        conn.close()
    except pyodbc.Error as e:
        raise Exception(f"❌ Error querying SQL Server: {e}")
    except Exception as e:
        raise Exception(f"❌ Unexpected error querying SQL Server: {e}")
    return columns


def get_columns_postgres(target, database, schema, identifier) -> List[Tuple[str, str]]:
    if psycopg2 is None:
        raise Exception(
            "❌ psycopg2 is not installed. Please install it with 'pip install psycopg2-binary'."
        )

    columns = []
    try:
        conn = psycopg2.connect(
            dbname=target.get("dbname", database),
            user=target.get("user"),
            password=target.get("password") or target.get("pass"),
            host=target.get("host"),
            port=target.get("port", 5432),
        )
        cursor = conn.cursor()
        query = """
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = %s AND table_name = %s
            ORDER BY ordinal_position;
        """
        cursor.execute(query, (schema, identifier))
        fetched_columns = cursor.fetchall()
        if not fetched_columns:
            # No columns found; table does not exist
            raise Exception(
                f"❌ Error: Table '{identifier}' does not exist in schema '{schema}' of database '{database}'."
            )
        columns = [(row[0], row[1]) for row in fetched_columns]
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        raise Exception(f"❌ Error querying PostgreSQL: {e}")
    except Exception as e:
        raise Exception(f"❌ Unexpected error querying PostgreSQL: {e}")
    return columns


def get_columns_redshift(target, database, schema, identifier) -> List[Tuple[str, str]]:
    # Redshift uses the same driver as PostgreSQL
    return get_columns_postgres(target, database, schema, identifier)


def get_columns_snowflake(
    target, database, schema, identifier
) -> List[Tuple[str, str]]:
    if snowflake is None:
        raise Exception(
            "❌ snowflake-connector-python is not installed. Please install it with 'pip install snowflake-connector-python'."
        )

    columns = []
    try:
        conn = snowflake.connector.connect(
            user=target.get("user"),
            password=target.get("password") or target.get("pass"),
            account=target.get("account"),
            database=database,
            schema=schema,
            role=target.get("role"),
            warehouse=target.get("warehouse"),
        )
        cursor = conn.cursor()
        query = """
            SELECT COLUMN_NAME, DATA_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
            ORDER BY ORDINAL_POSITION;
        """
        cursor.execute(query, (schema.upper(), identifier.upper()))
        fetched_columns = cursor.fetchall()
        if not fetched_columns:
            # No columns found; table does not exist
            raise Exception(
                f"❌ Error: Table '{identifier}' does not exist in schema '{schema}' of database '{database}'."
            )
        columns = [(row[0], row[1]) for row in fetched_columns]
        cursor.close()
        conn.close()
    except snowflake.connector.errors.ProgrammingError as e:
        raise Exception(f"❌ Error querying Snowflake: {e}")
    except Exception as e:
        raise Exception(f"❌ Unexpected error querying Snowflake: {e}")
    return columns


def get_columns_bigquery(target, database, schema, identifier) -> List[Tuple[str, str]]:
    if bigquery is None:
        raise Exception(
            "❌ google-cloud-bigquery is not installed. Please install it with 'pip install google-cloud-bigquery'."
        )

    columns = []
    try:
        client = bigquery.Client(project=target.get("project"))
        dataset_ref = client.dataset(schema)
        table_ref = dataset_ref.table(identifier)
        table = client.get_table(table_ref)
        if not table.schema:
            raise Exception(
                f"❌ Error: Table '{identifier}' does not exist in schema '{schema}' of project '{target.get('project')}'."
            )
        columns = [(field.name, field.field_type.lower()) for field in table.schema]
    except bigquery.NotFound:
        raise Exception(
            f"❌ Error: Table '{identifier}' does not exist in schema '{schema}' of project '{target.get('project')}'."
        )
    except Exception as e:
        raise Exception(f"❌ Error querying BigQuery: {e}")
    return columns
