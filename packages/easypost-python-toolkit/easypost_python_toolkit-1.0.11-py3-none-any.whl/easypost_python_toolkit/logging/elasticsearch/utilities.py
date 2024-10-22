"""
This module provides utility functions used by the ElasticsearchLogger class for handling common tasks such as
generating index names, creating default documents, and validating input data. These functions are intended for
internal use within the module.

The utility functions assist in ensuring that documents are correctly formatted and that index names follow
a consistent naming convention with a date suffix.

Functions:
    - _generate_index_name: Generates an index name with a date suffix based on the base index name.
    - _generate_default_document: Creates a default document structure with a timestamp and message.
    - _validate_document: Validates that the provided document is a dictionary.
    - _validate_index_name: Validates that the provided index name is a non-empty string.
"""

from datetime import datetime


def generate_index_name(base_index: str):
    """Generate an index name with a date suffix."""
    date_suffix = datetime.today().strftime("%Y.%m.%d")
    return f"{base_index}_logging_{date_suffix}"


def generate_default_document(message: str):
    """Generate a default document with a timestamp and message."""
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "message": message,
    }


def validate_document(document):
    """Validate that the document is a dictionary."""
    if not isinstance(document, dict):
        raise ValueError("Document must be a dictionary")


def validate_index_name(index):
    """Validate that the index name is a non-empty string."""
    if not isinstance(index, str) or not index:
        raise ValueError("Index name must be a non-empty string")
