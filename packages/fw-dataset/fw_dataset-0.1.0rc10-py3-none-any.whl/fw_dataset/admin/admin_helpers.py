"""Helper functions for the admin module."""

import csv
import hashlib
import json
import random
import re
from ast import literal_eval as safe_eval
from pathlib import Path
from typing import Dict, Union

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from deepdiff import DeepDiff
from duckdb import DuckDBPyConnection
from flywheel.models.mixins import ContainerBase as Container
from fsspec import AbstractFileSystem
from pyarrow import dataset as ds

from ..models import DataModel, Dataset
from .constants import TABULAR_DATA_SCHEMA

# Dictionary to map Pandas data types to JSON schema types
TYPE_TO_SCHEMA = {
    "string": "string",
    "float64": "number",
    "int64": "integer",
    "bool": "boolean",
    "object": "string",
    "datetime64[ns, tzutc()]": "datetime64[ns]",
}

# Dictionary to map JSON schema types to default values
TYPE_DEFAULTS = {
    "string": "",
    "number": 0,
    "integer": 0,
    "boolean": False,
    "object": {},
}

# Dictionary to map JSON schema types to Python types
# Used for conversion of values to enforce schema types
SCHEMA_TO_TYPE = {
    "string": str,
    "number": float,
    "integer": int,
    "boolean": bool,
    "object": dict,
}


def register_arrow_virtual_table(
    conn: DuckDBPyConnection,
    filesystem: AbstractFileSystem,
    table_id: str,
    table_path: Path,
    file_format: str = "parquet",
) -> None:
    """Register an arrow table as a virtual table in the database.

    data_path can be a directory containing multiple parquet files or a single parquet
    file.

    Args:
        conn (DuckDBPyConnection): The connection to the DuckDB database
        table_id (str): The table id
        table_path (Path): The path to the parquet file(s)
        file_format (str): The file format of the data. Defaults to "parquet".
    """
    existing_tables = conn.execute("SHOW TABLES").fetchdf()
    existing_tables = existing_tables["name"].tolist()
    if table_id not in existing_tables:
        dataset = ds.dataset(str(table_path), format=file_format, filesystem=filesystem)
        scanner = ds.Scanner.from_dataset(dataset)
        conn.register(table_id, scanner)


def save_schema(
    filesystem: AbstractFileSystem,
    schemas_path: Path,
    schema_name: str,
    schema: dict,
    overwrite: bool = False,
) -> None:
    """Save schema to the dataset directory.

    Args:
        filesystem (AbstractFileSystem): The filesystem object to use.
        schemas_path (Path): The path to the dataset schemas.
        schema_key (str): The key of the schema.
        schema (dict): The schema to save.
        overwrite (bool, optional): Overwrite the schema if it exists. Defaults to False.
    """
    schema_path = schemas_path / f"{schema_name}.schema.json"
    filesystem.makedirs(str(schema_path.parent), exist_ok=True)
    if not filesystem.exists(str(schema_path)) or overwrite:
        with filesystem.open(str(schema_path), "w") as f:
            json.dump(
                schema,
                f,
                indent=4,
                default=str,
            )


def save_table(
    filesystem: AbstractFileSystem,
    tables_path: Path,
    table_name,
    table_df,
    partition=None,
) -> None:
    """Save a table to the dataset directory.

    # TODO: Create a way to update a table, append, or overwrite it.
    # TODO: This is where we can save the table_df with field partitions.

    Args:
        filesystem (AbstractFileSystem): The filesystem object to use.
        tables_path (Path): The path to the tables of the dataset.
        table_name (str): The name of the table.
        table_df (pd.DataFrame): The dataframe to save.
        partition (str, optional): The partition of the table. Defaults to None.
    """
    table_path = f"{tables_path}/{table_name}"

    filesystem.makedirs(table_path, exist_ok=True)
    if partition:
        table_path_file = f"{table_path}/{partition}.parquet"
    else:
        table_path_file = f"{table_path}/{table_name}.parquet"

    if not filesystem.exists(table_path_file):
        with filesystem.open(table_path_file, "wb") as f:
            table_df.to_parquet(f)


def save_pyarrow_table(
    filesystem: AbstractFileSystem,
    tables_path: Path,
    table_name: str,
    table_df: pd.DataFrame,
    partition_cols: list | None = None,
) -> None:
    """Save a table to the dataset directory with a pyarrow table.

    This function enables the saving of tables with partitions and schema evolution.

    NOTE: Introducing partitioning on columns increases the size of the dataset (e.g.
    22 Mb w/o partitioning v.s. 2.0 Gb partitioning on subject_id and session_id).

    Schema evolution is the ability to add new columns to a table without breaking
    existing queries.

    Args:
        filesystem (AbstractFileSystem): The filesystem object to use.
        tables_path (Path): The path to the tables of the dataset.
        table_name (str): The name of the table.
        table_df (pd.DataFrame): The dataframe to save.
        partition_cols (list, optional): The columns of the dataframe to partition on. Defaults to None.
    """
    table_path = f"{tables_path}/{table_name}"

    # Create the "directory" structure
    filesystem.makedirs(table_path, exist_ok=True)

    # NOTE: The following code is necessary to convert object columns to string columns.
    #       This includes columns that have both integers and lists of integers.
    # TODO: An optimization would be to convert columns with int/list[int] to list[int].

    # Convert object columns to string columns
    for col in table_df.columns:
        if table_df[col].dtype == "O":
            table_df[col] = table_df[col].astype("string")

    # Convert pandas DataFrame to pyarrow Table
    table = pa.Table.from_pandas(table_df)

    # Write the dataset using the filesystem object
    pq.write_to_dataset(
        table,
        root_path=table_path,
        partition_cols=partition_cols,
        filesystem=filesystem,
    )


def convert_with_default(value, dtype, default):
    """Convert a value to a type with a default fallback.

    Args:
        value: Value to convert.
        dtype: The type to convert the value to.
        default: The default value if the conversion fails.

    Returns:
        variable_type: The converted or default value
    """
    # treat bools differently, since casting any non-empty string as bool
    # always returns True:
    if dtype is bool:
        value = str(value).lower()
        if value in ("y", "yes", "t", "true", "1"):
            return True
        elif value in ("n", "no", "f", "false", "0"):
            return False
        else:
            print("Invalid bool value %s", value)
            if isinstance(default, bool):
                return default
            else:
                return False

    # dtype is not bool:
    try:
        if not isinstance(value, dtype):
            if safe_eval(value) == dtype(value):
                return dtype(value)
            else:
                raise ValueError
        else:
            return dtype(value)
    except (ValueError, TypeError):
        return default


def enforce_field_types(
    schema: DataModel, table_df: pd.DataFrame, enforce: bool = False
) -> pd.DataFrame:
    """Use a schema to enforce field types on a table dataframe.

    Args:
        schema (DataModel): The schema to enforce on the table dataframe.
        table_df (pandas.Dataframe): The table dataframe to enforce the schema on.
        enforce (bool, optional): Enforce the schema on the table dataframe. Defaults to False.

    Returns:
        pandas.Dataframe: The table dataframe with enforced field types.
    """
    # Set up a template DataFrame with the expected columns and types
    template_columns = list(schema.properties.keys())
    template_types = [
        SCHEMA_TO_TYPE.get(prop["type"], str) for _, prop in schema.properties.items()
    ]
    template_df = pd.DataFrame(
        {col: pd.Series(dtype=dt) for col, dt in zip(template_columns, template_types)}
    )

    if table_df.empty:
        return template_df

    # Ensure we have a dataframe with all of the required columns
    table_df = pd.concat([template_df, table_df])

    table_dtypes = table_df.dtypes
    for property_ in schema.properties.keys():
        property_type_name = str(table_dtypes[str(property_)].name)
        if (
            TYPE_TO_SCHEMA.get(property_type_name, "string")
            != schema.properties[property_]["type"]
            or enforce
        ):
            try:
                table_df[property_] = table_df[property_].apply(
                    lambda x: convert_with_default(
                        x,
                        SCHEMA_TO_TYPE[schema.properties[property_]["type"]],
                        TYPE_DEFAULTS[schema.properties[property_]["type"]],
                    )
                )
            except:
                pass

    return table_df


def get_delimiter(filesystem, file_path, bytes_read=40960) -> str:
    """A function to get the delimiter of a csv file

    Args:
        file_path (Pathlike): The path to the file
        bytes (int, optional): The number of bytes to read. Defaults to 40960.

    Returns:
        str: The delimiter of the csv file
    """
    sniffer = csv.Sniffer()
    data = filesystem.open(file_path, "r", encoding="utf-8").read(bytes_read)
    delimiter = sniffer.sniff(data).delimiter
    return delimiter


def sanitize_table_name(table_name) -> str:
    """Sanitize table names to conform to GA4GH DataConnect requirements.

    Args:
        table_name (str): The table name to sanitize.

    Returns:
        str: The sanitized table name.
    """
    valid_pattern = re.compile(r"^[a-z](?:[a-z0-9_]*(?:\.[a-z_][a-z0-9_]*)?)*$")
    # Replace uppercase letters with lowercase
    table_name = table_name.lower()

    # Replace prohibited characters with underscore
    prohibited_chars = r'[!@#$%^&*()\-+=~`{}[\]|:;"\'<>,?\/\.\s]'
    table_name = re.sub(prohibited_chars, "_", table_name)

    # Replace digits following a "." with an underscore
    table_name = re.sub(r"\.(?=\d)", "._", table_name)

    # Remove leading invalid characters until a valid character is found
    while not valid_pattern.match(table_name):
        table_name = table_name[1:]
        if len(table_name) == 0:
            random.seed(42)
            table_name = f"table_{random.randint(100,999)}"

    return table_name


def add_parent_info(table_df, fw_file) -> pd.DataFrame:
    """Ensure that the parent information is added to the table dataframe.

    This is intended to be used with the tabular data schema and the custom
    info schema.

    Args:
        table_df (pandas.Dataframe): Dataframe to add parent information to.
        fw_file (dict): File dictionary from the Flywheel SDK to use as a source.

    Returns:
        pandas.Dataframe: Dataframe with parent information added.
    """
    # Get existing columns
    table_columns = list(table_df.columns)

    parent_attributes = TABULAR_DATA_SCHEMA.required
    for attr in parent_attributes:
        attr_split = attr.split(".")
        sub_attr = attr_split[1]
        # Add the parent information to the table
        if sub_attr != "file":
            table_df[attr] = fw_file[attr_split[0]][sub_attr]
        # Else add the "parents.file" information to the table
        else:
            table_df[attr] = fw_file["file_id"]

        # Remove the attribute from the list of columns
        if attr in table_columns:
            table_columns.remove(attr)

    # Move the identifying attributes to the front
    table_columns = parent_attributes + table_columns
    table_df = table_df[table_columns]

    return table_df


def get_table_schema(filesystem, file_path=None, table_df=None, schema=None):
    """A function to get the schema of a csv file or dataframe.

    Open a csv file and read the first 1000 rows to estimate the data types of the
    columns. If we are given a DataFrame, we can use that to estimate the schema.
    A schema can be provided as a starting point.

    Args:
        file_path (Pathlike, optional): Path to a tabular data file. Defaults to None.
        table_df (pandas.DataFrame, optional): Populated DataFrame. Defaults to None.
        schema (dict, optional): The schema to use as template. Defaults to None.

    Returns:
        dict: The schema of the csv file/dataframe.
    """
    if file_path is None and table_df is None:
        raise ValueError("Either file_path or table_df must be provided.")

    if file_path and filesystem.exists(file_path):
        try:
            # Get the delimiter of the file
            delimiter = get_delimiter(filesystem, file_path)
            # Read the first 1000 rows of the file to estimate the data types
            # TODO: Other "tabular data" types need to be supported. CSV is the only one
            # currently supported.
            table_df = pd.read_csv(
                filesystem.open(file_path), delimiter=delimiter, nrows=1000, comment="#"
            )
        except Exception as e:
            print(f"Error reading file: {file_path}")
            print(e)
            raise ValueError("Error reading file.") from e
    elif table_df is None:
        raise ValueError("Either file_path or table_df must be provided.")

    # If a schema is not provided, use the tabular data schema as a starting point
    if not schema:
        schema = TABULAR_DATA_SCHEMA.model_dump(mode="json")

    for col in table_df.columns:
        # TODO: This location is a good place to check and enforce the type of the
        # column
        # If the column is in the schema, preserve the entry
        if col not in schema["properties"].keys():
            schema["properties"][col] = {
                "type": TYPE_TO_SCHEMA[str(table_df[col].dtype)],
                "description": "",
            }
            schema["required"].append(col)

    return schema


def match_table_schema(matched_schemas: dict, schema_to_match: dict) -> str | None:
    """Match a schema to a list of schemas.

    NOTE: Eventually, scan the columns of the table and infer the data
    type of each column. Enforce a numeric type if the column is numeric,
    a string type if the column is a string, and a boolean type if the column is a
    boolean.

    TODO: This is the function to update with AI-driven schema matching.

    Args:
        schemas (dict): The list of schemas to match against
        schema_to_match (dict): The schema to match

    Returns:
        string: The key of the matched schema or None
    """
    for k, schema in matched_schemas.items():
        # TODO: a better matching protocol here
        ddiff = DeepDiff(
            schema["properties"], schema_to_match["properties"], ignore_order=True
        )
        if not ddiff:
            return k
        else:
            keys = [
                "dictionary_item_added",
                "dictionary_item_removed",
                "values_changed",
            ]
            num_diff = sum([len(ddiff[key]) for key in keys if ddiff.get(key)])
            # If the number of differences is less than 10% of the number of columns
            # in the schema, then consider the schemas to be the same
            # TODO: Make this a configurable parameter
            if num_diff / len(schema["properties"]) < 0.1:
                return k
    return None


def get_container_path(container_record: Union[Dict, Container]) -> Path:
    """Get the path of a container for saving files and info.

    Args:
        container_record (dict|Container): The container record to get the path from.

    Returns:
        Pathlike: The parent path of the container.

    Raises:
        ValueError: If the container_record is not a dict or a Container object.
    """
    if not isinstance(container_record, (Dict, Container)):
        raise ValueError("container_record must be a dict or a Container object.")

    container_path = Path(".")
    for parent in [
        "group",
        "project",
        "subject",
        "session",
        "acquisition",
        "analysis",
    ]:
        if container_record.get("parents") and container_record.get("parents", {}).get(
            parent
        ):
            container_path /= container_record["parents"][parent]

    if isinstance(container_record, Container):
        container_id = container_record.id
    elif isinstance(container_record, Dict):
        container_id = container_record["id"]

    # Always add the container id
    container_path /= container_id

    return container_path


def validate_dataset_table(duckdb_conn, filesystem, dataset, table_name) -> bool:
    """Validate a dataset table.

    Examines the dataset path, table path, and the table itself to ensure that the table
    is valid and non-empty.

    Args:
        duckdb_conn (duckdb.Connection): The DuckDB connection to use.
        filesystem (AbstractFileSystem): The filesystem object to use.
        dataset (Dataset): The Dataset Object.
        table_name (str): The name of the table to validate.

    Returns:
        bool: True if the table is valid, False otherwise.
    """
    # Ensure the dataset path exists
    dataset_path = dataset.paths.dataset_path
    if not filesystem.exists(dataset_path):
        # TODO: Turn all print statements into logging statements
        print(f"Dataset path {dataset_path} does not exist.")
        return False

    table_path = dataset.paths.tables_path / table_name
    if not filesystem.exists(table_path):
        print(f'The "{table_name}" table does not exist: {table_path}')
        return False

    try:
        register_arrow_virtual_table(duckdb_conn, filesystem, table_name, table_path)

        # Ensure the files table is not empty
        files_count = duckdb_conn.execute(
            f"SELECT COUNT(*) FROM {table_name}"
        ).fetchone()[0]
        return files_count > 0

    except Exception as e:
        print(f'Error registering the "{table_name}" table: {e}')
        return False


def save_custom_info_table(
    dataset: Dataset, custom_info_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Save a custom information table partition to the specified dataset path.

    Args:
        dataset (Dataset): The dataset object.
        custom_info_df (pd.DataFrame): The custom information table to be saved.
    Returns:
        pd.DataFrame: An empty DataFrame with the same columns as the custom_info_df.
    """
    if not custom_info_df.empty:
        # Create a hash key for the custom information table partition being saved
        hash_data = custom_info_df.iloc[0].to_dict()
        hash_str = json.dumps(hash_data, sort_keys=True)
        hash_key = hashlib.sha256(hash_str.encode()).hexdigest()
        # TODO: Use `save_pyarrow_table` to save the custom information table. This will
        # automatically create hashed parquet file names.
        save_table(
            dataset._fs,
            dataset.paths.tables_path,
            "custom_info",
            custom_info_df,
            partition=hash_key,
        )

    return pd.DataFrame(columns=custom_info_df.columns)
