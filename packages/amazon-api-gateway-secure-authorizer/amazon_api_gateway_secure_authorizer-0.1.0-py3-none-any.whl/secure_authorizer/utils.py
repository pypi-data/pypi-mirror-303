"""
utils.py: Utility functions for AWS Lambda authorizer.

This module provides helper functions for interacting with AWS Secrets Manager and handling
errors during the authorization process.

Functions:
- fetch_secret_value: Retrieves a specified version of a secret from AWS Secrets Manager.
- constant_time_compare: Compares two strings using a constant-time algorithm to prevent
timing attacks.

Logging:
- Detailed error logging is provided when secrets cannot be retrieved or decrypted.
"""

import os
import json
import hmac
import logging

import boto3
from botocore.exceptions import ClientError

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if os.getenv("DEBUG_MODE") == "1" else logging.INFO)


def fetch_secret_value(secret_id: str, key_name: str, version_stage: str = 'AWSCURRENT') -> str:
    """
    Fetch a specific version of the secret from AWS Secrets Manager.

    Args:
        secret_id (str): The secret identifier (name or ARN) in Secrets Manager.
        key_name (str): The specific key within the secret JSON that holds the API key.
        version_stage (str): The version stage of the secret (defaults to 'AWSCURRENT').

    Returns:
        str: The API key from the specified secret version.

    Raises:
        ClientError: If the secret cannot be retrieved or decrypted.
    """

    # AWS Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')

    try:
        secret = client.get_secret_value(SecretId=secret_id, VersionStage=version_stage)
        secret_json = json.loads(secret['SecretString'])
        if key_name not in secret_json:
            logger.error("Key %s not found in the secret %s", key_name, secret_id)
            raise KeyError(f"Key {key_name} not found in the secret {secret_id}")
        return str(secret_json[key_name])

    except ClientError as e:
        logger.error(
            "Failed to retrieve %s secret for %s: %s",
            version_stage,
            secret_id,
            e.response['Error']['Code']
        )
        raise e

    except json.JSONDecodeError as e:
        logger.error("Failed to parse the secret JSON for %s: %s", secret_id, str(e))
        raise ValueError(f"Invalid JSON in secret {secret_id}") from e


def constant_time_compare(val1: str, val2: str) -> bool:
    """
    Compare two strings using a constant-time algorithm to prevent timing attacks.

    Args:
        val1 (str): The first string to compare.
        val2 (str): The second string to compare.

    Returns:
        bool: True if the strings are equal, False otherwise.
    """
    return hmac.compare_digest(val1, val2)
