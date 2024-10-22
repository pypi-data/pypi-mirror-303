"""
This module provides a class, ElasticsearchLogger, for logging data to an Elasticsearch cluster.
The class supports logging individual documents, bulk logging of documents, and logging messages as documents.

The module utilizes utility functions from the `utilities` module to generate index names and validate both index names
and documents. Index names are always suffixed with a date. This way, data retention is simpler to set up.

Classes:
    ElasticsearchLogger: Provides methods for connecting to an Elasticsearch cluster and logging data.

Methods:
    - log_document: Logs a single document to the specified Elasticsearch index.
    - log_message: Logs a single message as a document to the specified Elasticsearch index.
    - log_bulk_documents: Logs multiple documents to the specified Elasticsearch index in bulk.
    - log_bulk_messages: Logs multiple messages as documents to the specified Elasticsearch index in bulk.

Usage:
    1. Initialize the ElasticsearchLogger class with the required Elasticsearch API key and host details.
    2. Use the provided methods to log documents or messages to the specified Elasticsearch index.
"""


import os

from elasticsearch import Elasticsearch

import utilities


class ElasticsearchLogger:
    def __init__(self, api_key_env_variable: str, default_index: str, host: str = 'https://elasticsearch-es-http.elastic-system.svc:9200/',
                 verify_certs: bool = False):
        try:
            self._default_index = default_index
            self._client = Elasticsearch(host, verify_certs=verify_certs, api_key=os.getenv(api_key_env_variable))
        except Exception as e:
            raise e

    def log_document(self, document: dict, index: str = None):
        """
        Log a single document to the specified Elasticsearch index.

        Args:
            document (dict): The document to log.
            index (str): The name of the Elasticsearch index. If not provided, the default index will be used.

        Returns:
            dict: The response from Elasticsearch after attempting to index the document.

        Raises:
            RuntimeError: If there is an issue logging the document to Elasticsearch.
        """

        try:
            index_name = utilities.generate_index_name(index or self._default_index)

            utilities.validate_index_name(index_name)
            utilities.validate_document(document)

            return self._client.index(index=index_name, body=document)
        except Exception as e:
            raise RuntimeError(f"Failed to log document to Elasticsearch: {e}")

    def log_message(self, message: str, index: str = None):
        """
        Log a single message as a document to the specified Elasticsearch index.

        Args:
            message (str): The message to log as a document.
            index (str): The name of the Elasticsearch index. If not provided, the default index will be used.

        Raises:
            RuntimeError: If there is an issue logging the message to Elasticsearch.
        """
        document = utilities.generate_default_document(message)
        self.log_document(document, index)

    def log_bulk_documents(self, documents: list[dict], index: str = None):
        """
        Log multiple documents to the specified Elasticsearch index in bulk.

        Args:
            documents (list[dict]): A list of documents to log.
            index (str): The name of the Elasticsearch index. If not provided, the default index will be used.

        Returns:
            dict: The response from Elasticsearch after attempting to index the documents in bulk.

        Raises:
            RuntimeError: If there is an issue logging the documents to Elasticsearch.
        """
        try:
            index_name = utilities.generate_index_name(index or self._default_index)

            utilities.validate_index_name(index_name)

            actions = [{"_index": index_name, "_source": doc} for doc in documents]
            return self._client.bulk(actions)
        except Exception as e:
            raise RuntimeError(f"Failed to log documents to Elasticsearch: {e}")

    def log_bulk_messages(self, messages: list[str], index: str = None):
        """
        Log multiple messages as documents to the specified Elasticsearch index in bulk.

        Args:
            messages (list[str]): A list of messages to log as documents.
            index (str): The name of the Elasticsearch index. If not provided, the default index will be used.

        Returns:
            dict: The response from Elasticsearch after attempting to index the messages in bulk.

        Raises:
            RuntimeError: If there is an issue logging the messages to Elasticsearch.
        """
        documents = [utilities.generate_default_document(message) for message in messages]
        return self.log_bulk_documents(documents, index)

