import json
import re
from gzip import GzipFile
from typing import Dict
from urllib import parse

import fsspec
from adlfs import AzureBlobFileSystem
from fsspec import AbstractFileSystem
from fsspec.implementations.local import LocalFileSystem
from gcsfs import GCSFileSystem
from s3fs import S3FileSystem


def decompress_stream(input_stream):
    with GzipFile(fileobj=input_stream, mode="rb") as gz_file:
        while True:
            chunk = gz_file.read(8192)  # Read in 8KB chunks
            if not chunk:
                break
            yield chunk


def _get_storage_credentials(api_client, fs_type: str, storage_id: str) -> dict:
    """Get the storage credentials for a dataset.

    Retrieves the storage credentials for a dataset from the registered storage for
    this dataset and the project it is associated with.

    Args:
        fs_type (str): The type of filesystem to use. Options are "s3", "gs", "az", "fs", "local".
        storage_id (str): The storage_id for the Flywheel storage filesystem.

    Raises:
        ValueError: If Storage credentials are not found for the dataset.
        ValueError: If Storage type mismatch.

    Returns:
        dict: The storage credentials for the dataset.
    """
    storage_creds = None
    if fs_type and storage_id:
        storage = api_client.get(f"/xfer/storages/{storage_id}")
        storage_creds = api_client.get(f"/xfer/storage-creds/{storage_id}")
        if not storage_creds:
            raise ValueError(
                f"Storage credentials not found for storage_id: {storage_id}"
            )
        if storage["config"]["type"] != fs_type:
            raise ValueError(
                f"Storage type mismatch: {storage['config']['type']} != {fs_type}"
            )
    elif not storage_creds:
        raise ValueError("Storage credentials not found for dataset")

    return storage_creds


def get_storage_filesystem(
    fs_type: str, storage_creds: Dict[str, str]
) -> AbstractFileSystem:
    """Get a storage filesystem object.

    TODO: We should be able to extract the fs-type directly from the storage_creds.

    Args:
        fs_type (str): The filesystem type, e.g., 's3', 'gs', 'az', 'fs', 'local'.
        storage_creds (Dict[str, str]): The storage credentials for the filesystem.

    Raises:
        ValueError: On Unsupported storage type.

    Returns:
        AbstractFileSystem: Initialized filesystem object.
    """

    filesystem = None

    # TODO: Replace the following with fsspec filesystems
    #       https://filesystem-spec.readthedocs.io/en/latest/
    # NOTE: The following code--as well as the above reference--supports the use of
    #       tokens, refresh tokens, and other authentication methods.
    match fs_type:
        case "s3":
            filesystem = get_s3_filesystem(storage_creds)
        case "gs":
            filesystem = get_gcs_filesystem(storage_creds)
        case "az":
            filesystem = get_az_filesystem(storage_creds)
        case "fs" | "local":
            filesystem = get_fs_filesystem()
        case _:
            raise ValueError(f"Unsupported storage type: {fs_type}")
    return filesystem


def get_s3_filesystem(storage_creds: Dict[str, str]) -> S3FileSystem:
    """Get an S3 Filesystem object.

    The storage credentials for the S3 Filesystem are passed in as a dictionary that
    must have the following format:

    {'url': 's3://{bucket}?access_key_id={access_key_id}&secret_access_key={secret_access_key}'}

    Args:
        storage_creds (Dict[str,str]): The storage credentials for the S3 Filesystem.

    Returns:
        S3FileSystem: An S3 Filesystem object.
    """
    parsed_url = parse.urlparse(storage_creds["url"])
    query_params = dict(re.findall(r"([^&=]+)=([^&]*)", parsed_url.query))
    key = query_params["access_key_id"]
    secret = query_params["secret_access_key"]
    return fsspec.filesystem("s3", key=key, secret=secret)
    # return S3FileSystem(key=key, secret=secret)


def get_gcs_filesystem(storage_creds: Dict[str, str]) -> GCSFileSystem:
    """Get a GCS Filesystem object.

    The storage credentials for the GCS Filesystem are passed in as a dictionary that
    must have the following format:

    {'url': 'gs://{bucket}?application_credentials={
        "type": "service_account",
        "project_id": "{project_id}",
        "private_key_id": "{private_key_id}",
        "private_key": "{private_key}",
        "client_email": "{email}",
        "client_id": "{client_id}",
        "auth_uri":"{auth_uri}",
        "token_uri":"{token_uri}",
        "auth_provider_x509_cert_url":"{auth_provider_x509_cert_url}",
        "client_x509_cert_url":"{client_x509_cert_url}",
        "universe_domain": "googleapis.com"
        }'
    }

    Args:
        storage_creds (Dict[str,str]): The storage credentials for the GCS Filesystem.

    Returns:
        GCSFileSystem: A GCS Filesystem object.
    """
    _, _, creds_json = storage_creds["url"].partition("=")
    credentials = json.loads(creds_json)
    return fsspec.filesystem("gs", token=credentials)
    # return GCSFileSystem(token=credentials)


def get_az_filesystem(storage_creds: dict) -> AzureBlobFileSystem:
    """Get an Azure Blob Filesystem object.

    The storage credentials for the Azure Blob Filesystem are passed in as a dictionary
    that must have the following format:
    {'url': 'az://{account_name}.blob.core.windows.net/{container}?access_key={access_key}'}

    Args:
        storage_creds (str): The storage credentials for the Azure Blob Filesystem.

    Returns:
        AzureBlobFileSystem: An Azure Blob Filesystem object.
    """
    parsed_url = parse.urlparse(storage_creds["url"])
    query_params = dict(re.findall(r"([^&=]+)=([^&]*)", parsed_url.query))
    query_params["account_name"] = parsed_url.netloc.split(".")[0]
    query_params["container"] = parsed_url.path[1:]

    account_name = query_params["account_name"]
    account_key = query_params["access_key"]
    return fsspec.filesystem("az", account_name=account_name, account_key=account_key)
    # return AzureBlobFileSystem(account_name=account_name, account_key=account_key)


def get_fs_filesystem() -> LocalFileSystem:
    """This is a placeholder for a local filesystem.

    The local filesystem will point to a directory on the local machine where the
    dataset is stored. This is useful for hosting a dataset on a local machine or a
    VM where the dataset is not stored in a cloud storage bucket.

    Returns:
        Path: The local filesystem object.
    """
    """This should return a filesystem object for a local directory
    but what that is going to look like is another question.
    """
    return fsspec.filesystem("file")
