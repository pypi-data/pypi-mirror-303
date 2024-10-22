"""
authorizer.py AWS Lambda authorizer for Amazon API Gateway.

This module defines the Lambda handler function responsible for authorizing incoming requests
based on an API key provided in the headers. The key is validated against secrets stored in
AWS Secrets Manager, with both "current" and "pending" versions of the secret being checked.

It utilizes helper functions from the `utils` module for fetching secrets and handling
errors encountered while accessing AWS Secrets Manager.

Environment Variables:
- SECRET_NAME: The name of the secret in Secrets Manager that stores the API key.
- SECRET_KEY_NAME: The key name inside the secret's JSON structure that holds the API key.
- HEADER_NAME: The name of the HTTP header containing the API key.

Returns:
- A response indicating whether the request is authorized, in the format required by API Gateway.
"""

import os
import logging
from typing import Any

from .utils import fetch_secret_value, constant_time_compare

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if os.getenv("DEBUG_MODE") == "1" else logging.INFO)


def handler(event: dict[str, Any], context: Any) -> dict[str, bool]:  # pylint: disable=unused-argument
    """
    Lambda handler function for API Gateway custom authorizer.

    Args:
        event (dict): The incoming request payload from API Gateway, which includes headers.
        context (Any): The Lambda context object (unused).

    Returns:
        dict: A response dictionary indicating whether the request is authorized(`isAuthorized`
        key).
    """

    # Load environment variables
    secret_name: str = os.getenv('SECRET_NAME', "")
    secret_key_name: str = os.getenv('SECRET_KEY_NAME', "")
    header_name: str = os.getenv('HEADER_NAME', "x-origin-verify").lower()

    # Validate environment variables
    if not secret_name or not secret_key_name or not header_name:
        logger.error(
            "Environment variables SECRET_NAME, SECRET_KEY_NAME, or HEADER_NAME are missing."
        )
        raise ValueError("Required environment variables are missing.")

    # Get headers in lowercase
    headers: dict[str, str] = {k.lower(): v for k, v in (event.get('headers') or {}).items()}
    # Retrieve the API key from headers
    provided_api_key: str | None = headers.get(header_name)
    # Default response: access denied
    response = {'isAuthorized': False}

    if not provided_api_key:
        logger.debug("Authorization failed: missing or empty authorization header.")
        return response

    # Fetch the current secret version
    api_key = fetch_secret_value(secret_name, secret_key_name)

    if constant_time_compare(api_key, provided_api_key):
        logger.info("Authorization succeeded: API key matches the current version.")
        response['isAuthorized'] = True
    else:
        logger.debug("API key did not match the current version. Checking pending version.")
        # Check the pending secret version if the current one doesn't match
        api_key_pending = fetch_secret_value(
            secret_name,
            secret_key_name,
            version_stage='AWSPENDING'
        )

        if constant_time_compare(api_key_pending, provided_api_key):
            logger.info("Authorization succeeded: API key matches the pending version.")
            response['isAuthorized'] = True
        else:
            logger.warning(
                "Authorization failed: neither current nor pending " + \
                "version matched the provided API key."
            )

    return response
