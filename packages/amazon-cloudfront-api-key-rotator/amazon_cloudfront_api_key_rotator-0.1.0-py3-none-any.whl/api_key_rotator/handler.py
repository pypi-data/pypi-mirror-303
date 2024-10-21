"""
handler.py: This module defines the Lambda function handler for rotating API keys stored
in AWS Secrets Manager and updating the corresponding CloudFront distribution with the new API key.

The Lambda function processes events triggered by AWS Secrets Manager during a secret rotation 
process. It performs the following steps:

1. **createSecret**: Generates a new secret (API key) and stores it in the "AWSPENDING" version
stage.
2. **setSecret**: Updates the CloudFront distribution with the new API key.
3. **testSecret**: Verifies that the newly rotated API key works by testing against the origin.
4. **finishSecret**: Marks the newly rotated API key as "AWSCURRENT" to finalize the rotation
process.

The handler function is invoked with an event that specifies the current step in the secret 
rotation process, and it dispatches the appropriate function for each step.

Environment Variables:
- `CLOUDFRONT_DISTRIBUTION_ID`: The ID of the CloudFront distribution to update.
- `HEADER_NAME`: The name of the custom header used to pass the API key to the origin.
- `ORIGIN_URL`: The origin URL for testing the API key.
- `SECRET_KEY_NAME`: The key name under which the API key is stored in Secrets Manager.
- `SECRET_KEY_LENGTH`: The length of the generated API key.
"""

import json
import logging
from typing import Any

import boto3
from . import utils

# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: dict, context: Any) -> None:  # pylint: disable=unused-argument
    """
    Main Lambda handler function to rotate the API key.

    Args:
        event (dict): The event data passed to the Lambda function.
        context (Any): The runtime context of the Lambda function.

    Raises:
        ValueError: If the event structure is incorrect or a step is invalid.
    """
    logger.info("Received event: %s", json.dumps(event))

    arn = event.get('SecretId')
    token = event.get('ClientRequestToken')
    step = event.get('Step')

    if not arn or not token or not step:
        raise ValueError("Invalid event structure: missing required fields.")

    service_client = boto3.client('secretsmanager')
    metadata = service_client.describe_secret(SecretId=arn)

    if not metadata.get('RotationEnabled'):
        raise ValueError(f"Rotation is disabled for secret {arn}.")

    versions = metadata['VersionIdsToStages']
    if token not in versions:
        raise ValueError(f"Secret version {token} has no stage for rotation of secret {arn}.")
    if 'AWSCURRENT' in versions[token]:
        logger.info(
            "Secret version %s is already set as AWSCURRENT for %s.",
            token,
            arn
        )
        return
    if 'AWSPENDING' not in versions[token]:
        raise ValueError(
            f"Secret version {token} is not set as AWSPENDING for rotation of {arn}."
        )

    # Handle each rotation step
    if step == 'createSecret':
        utils.create_secret(service_client, arn, token)
    elif step == 'setSecret':
        utils.set_secret(service_client, arn, token)
    elif step == 'testSecret':
        utils.test_secret(service_client, arn, token)
    elif step == 'finishSecret':
        utils.finish_secret(service_client, arn, token)
    else:
        raise ValueError(f"Invalid step parameter: {step}.")
