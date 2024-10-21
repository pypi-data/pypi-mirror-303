"""
utils.py: This module provides utility functions used in the process of rotating API keys stored
in AWS Secrets Manager and updating them in CloudFront distributions. These helper functions
perform various operations including secret creation, distribution updates, and origin testing.

Functions:
- **get_cloudfront_distribution**: Retrieves the CloudFront distribution details for a given
distribution ID.
- **get_cloudfront_distribution_config**: Retrieves the configuration details of a CloudFront
distribution.
- **update_cloudfront_distribution**: Updates the CloudFront distribution's custom header with
a new API key.
- **test_origin**: Tests the API key by sending a request to the origin and checking the response.
- **create_secret**: Generates a new secret and stores it in the "AWSPENDING" version stage.
- **set_secret**: Updates the CloudFront custom header with the new API key stored in "AWSPENDING".
- **test_secret**: Verifies that the "AWSPENDING" API key works by testing it against the origin.
- **finish_secret**: Marks the newly rotated API key as "AWSCURRENT" to finalize the secret
rotation.

The functions in this module are designed to work in conjunction with AWS Lambda to automate 
the secret rotation process.

Environment Variables:
- `CLOUDFRONT_DISTRIBUTION_ID`: The ID of the CloudFront distribution to be updated.
- `HEADER_NAME`: The custom header name used for passing the API key to the origin.
- `ORIGIN_URL`: The URL of the origin to test the API key against.
- `SECRET_KEY_NAME`: The key name under which the API key is stored in Secrets Manager.
- `SECRET_KEY_LENGTH`: The length of the generated API key.
"""

import os
import json
import logging
import http.client
from typing import Any
from urllib.parse import urlparse

import boto3
from botocore.exceptions import ClientError
from .exceptions import OriginTestFailedException

# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Load environment variables
CF_DISTRIBUTION_ID : str = os.getenv('CLOUDFRONT_DISTRIBUTION_ID')
HEADER_NAME : str = os.getenv('HEADER_NAME', "x-origin-verify")
ORIGIN_URL : str = os.getenv('ORIGIN_URL')
SECRET_KEY_NAME : str = os.getenv('SECRET_KEY_NAME', "HTTP_API_KEY")
SECRET_KEY_LENGTH : int = int(os.getenv('SECRET_KEY_LENGTH', "32"))


def get_cloudfront_distribution(distribution_id: str) -> dict:
    """
    Fetches details of the CloudFront distribution.

    Args:
        distribution_id (str): The ID of the CloudFront distribution.
    
    Returns:
        dict: The CloudFront distribution details.
    """
    client = boto3.client('cloudfront')
    return client.get_distribution(Id=distribution_id)


def get_cloudfront_distribution_config(distribution_id: str) -> dict:
    """
    Fetches the configuration of the CloudFront distribution.

    Args:
        distribution_id (str): The ID of the CloudFront distribution.

    Returns:
        dict: The CloudFront distribution configuration.
    """
    client = boto3.client('cloudfront')
    return client.get_distribution_config(Id=distribution_id)


def update_cloudfront_distribution(distribution_id: str, header_value: str) -> dict:
    """
    Updates the custom header in the CloudFront distribution with a new API key value.

    Args:
        distribution_id (str): The ID of the CloudFront distribution.
        header_value (str): The new API key value to be set in the custom header.

    Raises:
        ValueError: If no custom header is found or distribution is not in 'Deployed' state.

    Returns:
        dict: The response from updating the CloudFront distribution.
    """
    client = boto3.client('cloudfront')
    distribution_status = get_cloudfront_distribution(distribution_id)

    if 'Deployed' not in distribution_status['Distribution']['Status']:
        raise ValueError(f"Distribution {distribution_id} is not in 'Deployed' status.")

    distribution_config = get_cloudfront_distribution_config(distribution_id)
    header_found = False

    # Update the header value for all origins that have the target custom header
    for origin in distribution_config['DistributionConfig']['Origins']['Items']:
        if origin['CustomHeaders']['Quantity'] > 0:
            for header in origin['CustomHeaders']['Items']:
                if HEADER_NAME == header['HeaderName']:
                    logger.info(
                        "Updating custom header %s for origin %s.",
                        HEADER_NAME,
                        origin['Id']
                    )
                    header['HeaderValue'] = header_value
                    header_found = True
                else:
                    logger.info(
                        "Ignoring custom header %s for origin %s.",
                        header['HeaderName'],
                        origin['Id']
                    )

    if not header_found:
        raise ValueError(
            f"No custom header '{HEADER_NAME}' found in distribution {distribution_id}."
        )

    # Update the distribution with the modified configuration
    response = client.update_distribution(
        Id=distribution_id,
        IfMatch=distribution_config['ResponseMetadata']['HTTPHeaders']['etag'],
        DistributionConfig=distribution_config['DistributionConfig']
    )
    return response


def test_origin(url: str, secret: str) -> bool:
    """
    Test if the origin responds with status 200 when using the provided API key in the header.

    Args:
        url (str): The URL of the origin to be tested.
        secret (str): The API key to be used in the request header.

    Returns:
        bool: True if the origin responds with a 200 status code, False otherwise.
    """
    parsed_url = urlparse(url)
    conn = http.client.HTTPSConnection(parsed_url.netloc)

    # Set up headers with the secret API key
    headers = {HEADER_NAME: secret}

    # Make the request to the origin
    conn.request("GET", parsed_url.path or "/", headers=headers)

    # Get the response and check the status code
    response = conn.getresponse()
    return response.status == 200


def create_secret(service_client: Any, arn: str, token: str) -> None:
    """
    Creates a new secret and stores it as the AWSPENDING version in Secrets Manager.

    Args:
        service_client (Any): The Secrets Manager service client.
        arn (str): The ARN of the secret.
        token (str): The ClientRequestToken associated with the secret version.

    Raises:
        ClientError: If unable to create the secret.
    """
    try:
        service_client.get_secret_value(SecretId=arn, VersionStage='AWSCURRENT')
    except ClientError as e:
        logger.error("Error retrieving current secret: %s", str(e))
        raise

    try:
        service_client.get_secret_value(
            SecretId=arn,
            VersionId=token,
            VersionStage='AWSPENDING'
        )
        logger.info("Successfully retrieved AWSPENDING secret for %s.", arn)
    except service_client.exceptions.ResourceNotFoundException:
        password = service_client.get_random_password(
            PasswordLength=SECRET_KEY_LENGTH,
            ExcludePunctuation=True
        )
        secret_string = json.dumps({SECRET_KEY_NAME: password['RandomPassword']})

        service_client.put_secret_value(
            SecretId=arn,
            ClientRequestToken=token,
            SecretString=secret_string,
            VersionStages=['AWSPENDING']
        )
        logger.info(
            "Successfully put AWSPENDING secret for %s with version %s.",
            arn,
            token
        )


def set_secret(service_client: Any, arn: str, token: str) -> None:
    """
    Sets the AWSPENDING secret by updating the CloudFront distribution.

    Args:
        service_client (Any): The Secrets Manager service client.
        arn (str): The ARN of the secret.
        token (str): The ClientRequestToken associated with the secret version.
    
    Raises:
        ValueError: If the CloudFront distribution is not in 'Deployed' state.
    """
    pending = service_client.get_secret_value(
        SecretId=arn,
        VersionId=token,
        VersionStage='AWSPENDING'
    )
    pending_secret = json.loads(pending['SecretString'])

    try:
        update_cloudfront_distribution(CF_DISTRIBUTION_ID, pending_secret[SECRET_KEY_NAME])
        logger.info(
            "Successfully set new API key in CloudFront distribution %s.",
            CF_DISTRIBUTION_ID
        )
    except ClientError as e:
        logger.error("Failed to update CloudFront distribution: %s", str(e))
        raise


def test_secret(service_client: Any, arn: str, token: str) -> None:
    """
    Tests the AWSPENDING secret by making a request to the origin URL.

    Args:
        service_client (Any): The Secrets Manager service client.
        arn (str): The ARN of the secret.
        token (str): The ClientRequestToken associated with the secret version.

    Raises:
        Exception: If the test fails for either the pending or current secret.
    """
    pending = service_client.get_secret_value(
        SecretId=arn,
        VersionId=token,
        VersionStage='AWSPENDING'
    )
    current = service_client.get_secret_value(
        SecretId=arn,
        VersionStage='AWSCURRENT'
    )

    pending_secret = json.loads(pending['SecretString'])
    current_secret = json.loads(current['SecretString'])

    logger.info("Testing origin URL: %s", ORIGIN_URL)

    if not test_origin(ORIGIN_URL, pending_secret[SECRET_KEY_NAME]):
        raise OriginTestFailedException("AWSPENDING: API key test failed.")
    logger.info("AWSPENDING: API key test successful.")

    if not test_origin(ORIGIN_URL, current_secret[SECRET_KEY_NAME]):
        raise OriginTestFailedException("AWSCURRENT: API key test failed.")
    logger.info("AWSCURRENT: API key test successful.")


def finish_secret(service_client: Any, arn: str, token: str) -> None:
    """
    Marks the AWSPENDING secret as the AWSCURRENT secret, completing the rotation.

    Args:
        service_client (Any): The Secrets Manager service client.
        arn (str): The ARN of the secret.
        token (str): The ClientRequestToken associated with the secret version.
    """
    metadata = service_client.describe_secret(SecretId=arn)
    current_version = None

    for version, stages in metadata['VersionIdsToStages'].items():
        if 'AWSCURRENT' in stages:
            current_version = version
            break

    service_client.update_secret_version_stage(
        SecretId=arn,
        VersionStage='AWSCURRENT',
        MoveToVersionId=token,
        RemoveFromVersionId=current_version
    )
    logger.info(
        "Successfully promoted version %s to AWSCURRENT for secret %s.",
        token,
        arn
    )
