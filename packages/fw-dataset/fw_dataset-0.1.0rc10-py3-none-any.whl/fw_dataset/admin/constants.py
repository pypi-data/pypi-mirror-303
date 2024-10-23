import os
from pathlib import Path

from ..models import DataModel

#      This should be replaced with a PATH that is set by an environment variable, a
#      cli parameter, or a configuration file.
DEFAULT_DATAHOME = Path.home() / "fw-ga4gh-drs-gateway-data"
DATAHOME = Path(os.environ.get("FW_DATA_HOME", DEFAULT_DATAHOME))

# TODO: The SECRET_KEY should be stored in an environment variable or configuration file
DEFAULT_SECRET_KEY = "your_secret_key"
SECRET_KEY = os.environ.get("FW_SECRET_KEY", DEFAULT_SECRET_KEY)

# ALLOWED_INSTANCES restricts the Flywheel instances that can be accessed by the
# gateway. If this is not set, the gateway will allow access to any Flywheel instance.
# This should be a list of Flywheel URIs.
# e.g. ALLOWED_INSTANCES = ["latest.sse.flywheel.io","trial.flywheel.io"]
DEFAULT_ALLOWED_INSTANCES = []
# FW_ALLOWED_INSTANCES should be a colon-separated list of Flywheel URIs
env_allowed_instances = os.environ.get("FW_ALLOWED_INSTANCES")
ALLOWED_INSTANCES = (
    env_allowed_instances.split(":")
    if env_allowed_instances
    and isinstance(env_allowed_instances, str)
    and env_allowed_instances != ""
    else DEFAULT_ALLOWED_INSTANCES
)

# The maximum number of items that can be returned in a single page of results
PAGINATION_LIMIT = os.environ.get("PAGINATION_LIMIT", 100)

# The maximum time to spend waiting for a snapshot to be created
SNAPSHOT_TIMEOUT = os.environ.get("SNAPSHOT_TIMEOUT", 60 * 30)  # 30 minutes

# The default behavior for populating from tabular data and custom information
POPULATE_TABULAR_DATA = os.environ.get("POPULATE_TABULAR_DATA", "false") == "true"
POPULATE_CUSTOM_INFO = os.environ.get("POPULATE_CUSTOM_INFO", "false") == "true"

TIMESTAMP_PATTERN = (
    "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6}+00:00$"
)

# TODO: flywheel.SubjectOutput.swagger_types may give us all of the fields we need
SUBJECT_COLUMNS = [
    "id",
    "label",
    "age",
    "race",
    "ethnicity",
    "sex",
    "parents.group",
    "parents.project",
    "parents.subject",
    "parents.session",
    "parents.acquisition",
    "created",
    "modified",
]

SUBJECT_INFO = {
    "id": {
        "description": "The unique identifier for the subject",
        "pattern": "^[0-9a-f]{24}$",
        "type": "string",
    },
    "label": {
        "description": "The label for the subject",
        "pattern": "^[a-zA-Z0-9_\\-]+$",
        "type": "string",
    },
    "age": {
        "description": "The age of the subject",
        "type": "number",
    },
    "race": {
        "description": "The race of the subject",
        "type": "string",
    },
    "ethnicity": {
        "description": "The ethnicity of the subject",
        "type": "string",
    },
    "sex": {
        "description": "The sex of the subject",
        "type": "string",
        "enum": ["male", "female"],
    },
    "parents.group": {
        "description": "The group that the session belongs to",
        "type": "string",
    },
    "parents.project": {
        "description": "The project that the session belongs to",
        "type": "string",
    },
    "parents.subject": {
        "description": "The subject that the session belongs to",
        "type": "string",
    },
    "parents.session": {
        "description": "The session that the session belongs to",
        "type": "string",
    },
    "parents.acquisition": {
        "description": "The acquisition that the session belongs to",
        "type": "string",
    },
    "created": {
        "description": "The time the session was created",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
    "modified": {
        "description": "The time the session was last modified",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
}

SUBJECT_SCHEMA = DataModel(
    id="subjects",
    description="Subjects Table derived from View",
    properties=SUBJECT_INFO,
    required=SUBJECT_COLUMNS,
)

SESSION_COLUMNS = [
    "id",
    "label",
    "age",
    "weight",
    "parents.group",
    "parents.project",
    "parents.subject",
    "parents.session",
    "parents.acquisition",
    "created",
    "modified",
]

SESSION_INFO = {
    "id": {
        "description": "The unique identifier for the session",
        "pattern": "^[0-9a-f]{24}$",
        "type": "string",
    },
    "label": {
        "description": "The label for the session",
        "pattern": "^[a-zA-Z0-9_\\-]+$",
        "type": "string",
    },
    "age": {
        "description": "The age of the subject at the time of the session",
        "type": "number",
    },
    "weight": {
        "description": "The weight of the subject at the time of the session",
        "type": "number",
    },
    "parents.group": {
        "description": "The group that the session belongs to",
        "type": "string",
    },
    "parents.project": {
        "description": "The project that the session belongs to",
        "type": "string",
    },
    "parents.subject": {
        "description": "The subject that the session belongs to",
        "type": "string",
    },
    "parents.session": {
        "description": "The session that the session belongs to",
        "type": "string",
    },
    "parents.acquisition": {
        "description": "The acquisition that the session belongs to",
        "type": "string",
    },
    "created": {
        "description": "The time the session was created",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
    "modified": {
        "description": "The time the session was last modified",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
}

SESSION_SCHEMA = DataModel(
    id="sessions",
    description="Sessions Table derived from View",
    properties=SESSION_INFO,
    required=SESSION_COLUMNS,
)

ACQUISITION_COLUMNS = [
    "id",
    "label",
    "parents.group",
    "parents.project",
    "parents.subject",
    "parents.session",
    "parents.acquisition",
    "created",
    "modified",
]

ACQUISITION_INFO = {
    "id": {
        "description": "The unique identifier for the acquisition",
        "pattern": "^[0-9a-f]{24}$",
        "type": "string",
    },
    "label": {
        "description": "The label for the acquisition",
        "pattern": "^[a-zA-Z0-9_\\-]+$",
        "type": "string",
    },
    "parents.group": {
        "description": "The group that the acquisition belongs to",
        "type": "string",
    },
    "parents.project": {
        "description": "The project that the acquisition belongs to",
        "type": "string",
    },
    "parents.subject": {
        "description": "The subject that the acquisition belongs to",
        "type": "string",
    },
    "parents.session": {
        "description": "The session that the acquisition belongs to",
        "type": "string",
    },
    "parents.acquisition": {
        "description": "The acquisition that the acquisition belongs to",
        "type": "string",
    },
    "created": {
        "description": "The time the acquisition was created",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
    "modified": {
        "description": "The time the acquisition was last modified",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
}

ACQUISITION_SCHEMA = DataModel(
    id="acquisitions",
    description="Acquisitions Table derived from View",
    properties=ACQUISITION_INFO,
    required=ACQUISITION_COLUMNS,
)

ANALYSIS_COLUMNS = [
    "id",
    "label",
    "parents.group",
    "parents.project",
    "parents.subject",
    "parents.session",
    "parents.acquisition",
    "created",
    "modified",
    "gear_info.id",
    "gear_info.category",
    "gear_info.name",
    "gear_info.version",
]

ANALYSIS_INFO = {
    "id": {
        "description": "The unique identifier for the analysis",
        "pattern": "^[0-9a-f]{24}$",
        "type": "string",
    },
    "label": {
        "description": "The label for the analysis",
        "pattern": "^[a-zA-Z0-9_\\-]+$",
        "type": "string",
    },
    "parents.group": {
        "description": "The group that the analysis belongs to",
        "type": "string",
    },
    "parents.project": {
        "description": "The project that the analysis belongs to",
        "type": "string",
    },
    "parents.subject": {
        "description": "The subject that the analysis belongs to",
        "type": "string",
    },
    "parents.session": {
        "description": "The session that the analysis belongs to",
        "type": "string",
    },
    "parents.acquisition": {
        "description": "The acquisition that the analysis belongs to",
        "type": "string",
    },
    "created": {
        "description": "The time the analysis was created",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
    "modified": {
        "description": "The time the analysis was last modified",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
    "gear_info.id": {
        "description": "The ID of the gear",
        "type": "string",
    },
    "gear_info.category": {
        "description": "The category of the gear",
        "type": "string",
    },
    "gear_info.name": {
        "description": "The name of the gear",
        "type": "string",
    },
    "gear_info.version": {
        "description": "The version of the gear",
        "type": "string",
    },
}


ANALYSIS_SCHEMA = DataModel(
    id="analyses",
    description="Analyses Table derived from View",
    properties=ANALYSIS_INFO,
    required=ANALYSIS_COLUMNS,
)

FILE_COLUMNS = [
    "id",
    "file_id",
    "name",
    "size",
    "version",
    "parents.group",
    "parents.project",
    "parents.subject",
    "parents.session",
    "parents.acquisition",
    "parents.analysis",
    "created",
    "modified",
]

FILE_INFO = {
    "id": {
        "description": "The unique identifier for the file version",
        "pattern": "^[0-9a-f]{24}$",
        "type": "string",
    },
    "file_id": {
        "description": "The unique identifier for the file",
        "pattern": "^[0-9a-f]{24}$",
        "type": "string",
    },
    "version": {
        "description": "The version of the file",
        "type": "number",
    },
    "name": {
        "description": "The name of the file",
        "type": "string",
    },
    "size": {
        "description": "The size of the file in bytes",
        "type": "number",
    },
    "type": {
        "description": "The type of the file",
        "type": "string",
    },
    "mimetype": {
        "description": "The MIME type of the file",
        "type": "string",
    },
    "modality": {
        "description": "The modality of the file",
        "type": "string",
    },
    "deid_log_id": {
        "description": "The de-identification log ID of the file",
        "type": "string",
    },
    "tags": {
        "description": "The tags associated with the file",
        "type": "array",
        "items": {"type": "string"},
    },
    "hash": {
        "description": "The hash value of the file",
        "type": "string",
    },
    "replaced": {
        "description": "The file that this file replaced",
        "type": "string",
    },
    "zip_member_count": {
        "description": "The number of members in the ZIP file",
        "type": "number",
    },
    "origin.id": {
        "description": "The ID of the origin",
        "type": "string",
    },
    "origin.method": {
        "description": "The method of the origin",
        "type": "string",
    },
    "origin.type": {
        "description": "The type of the origin",
        "type": "string",
    },
    "origin.name": {
        "description": "The name of the origin",
        "type": "string",
    },
    "origin.via": {
        "description": "The via of the origin",
        "type": "string",
    },
    "parents.group": {
        "description": "The group that the file belongs to",
        "type": "string",
    },
    "parents.project": {
        "description": "The project that the file belongs to",
        "type": "string",
    },
    "parents.subject": {
        "description": "The subject that the file belongs to",
        "type": "string",
    },
    "parents.session": {
        "description": "The session that the file belongs to",
        "type": "string",
    },
    "parents.acquisition": {
        "description": "The acquisition that the file belongs to",
        "type": "string",
    },
    "parent_ref.type": {
        "description": "The type of the parent reference",
        "type": "string",
    },
    "parent_ref.id": {
        "description": "The ID of the parent reference",
        "type": "string",
    },
    "classification.Intent": {
        "description": "The intent classification of the file",
        "type": "array",
        "items": {"type": "string"},
    },
    "classification.Measurement": {
        "description": "The measurement classification of the file",
        "type": "array",
        "items": {"type": "string"},
    },
    "classification.Features": {
        "description": "The features classification of the file",
        "type": "array",
        "items": {"type": "string"},
    },
    "created": {
        "description": "The time the acquisition was created",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
    "modified": {
        "description": "The time the acquisition was last modified",
        "pattern": TIMESTAMP_PATTERN,
        "type": "string",
    },
}

FILE_SCHEMA = DataModel(
    id="files",
    description="Files Table Derived From Views and Container Data.",
    properties=FILE_INFO,
    required=FILE_COLUMNS,
    type="object",
)

TABULAR_DATA_SCHEMA = DataModel(
    **{
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "tabular_rasa",
        "description": "",
        "properties": {
            "parents.group": {
                "description": "The group that the file belongs to",
                "type": "string",
            },
            "parents.project": {
                "description": "The project that the file belongs to",
                "type": "string",
            },
            "parents.subject": {
                "description": "The subject that the file belongs to",
                "type": "string",
            },
            "parents.session": {
                "description": "The session that the file belongs to",
                "type": "string",
            },
            "parents.acquisition": {
                "description": "The acquisition that the file belongs to",
                "type": "string",
            },
            "parents.analysis": {
                "description": "The analysis that the file belongs to",
                "type": "string",
            },
            "parents.file": {
                "description": "The file id that the data of the row comes from",
                "type": "string",
            },
        },
        "required": [
            "parents.group",
            "parents.project",
            "parents.subject",
            "parents.session",
            "parents.acquisition",
            "parents.analysis",
            "parents.file",
        ],
        "type": "object",
    }
)

INFO_DICT = TABULAR_DATA_SCHEMA.model_dump()
INFO_DICT["properties"].update(
    {
        "custom_info": {
            "description": "Custom Information for container",
            "type": "string",
        }
    }
)
INFO_DICT["required"].append("custom_info")
INFO_DICT["$id"] = "custom_info"
INFO_SCHEMA = DataModel(**INFO_DICT)


TABLES = [
    {"id": "subjects", "name": "Subjects", "schema": SUBJECT_SCHEMA},
    {"id": "sessions", "name": "Sessions", "schema": SESSION_SCHEMA},
    {"id": "acquisitions", "name": "Acquisitions", "schema": ACQUISITION_SCHEMA},
    {"id": "analyses", "name": "Analyses", "schema": ANALYSIS_SCHEMA},
    {"id": "files", "name": "Files", "schema": FILE_SCHEMA},
]

# The mapping of the snapshot name to the table name, field mappings, and schema
# NOTE: snapshot table names and fields differ from the container names and properties
SNAPSHOT_MAPPINGS = {
    "subject": {
        "table_name": "subjects",
        "field_mappings": {"_id": "id"},
        "schema": SUBJECT_SCHEMA,
    },
    "session": {
        "table_name": "sessions",
        "field_mappings": {"_id": "id"},
        "schema": SESSION_SCHEMA,
    },
    "acquisition": {
        "table_name": "acquisitions",
        "field_mappings": {"_id": "id"},
        "schema": ACQUISITION_SCHEMA,
    },
    "analysis": {
        "table_name": "analyses",
        "field_mappings": {"_id": "id"},
        "schema": ANALYSIS_SCHEMA,
    },
    "file": {
        "table_name": "files",
        "field_mappings": {
            "_id.file_id": "file_id",
            "_id.version": "version",
            "uuid": "id",
        },
        "schema": FILE_SCHEMA,
    },
}
