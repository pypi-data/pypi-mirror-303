# API Key Rotator for Amazon CloudFront

In many architectures using Amazon [CloudFront](https://aws.amazon.com/cloudfront/) with [API Gateway](https://aws.amazon.com/api-gateway/), an API key is used to secure communication between CloudFront and the origin (API Gateway). This key is typically passed as a custom header in requests from CloudFront to the origin. While this setup enhances security, it's crucial to regularly rotate these API keys to maintain a robust security posture.

This project provides an automated solution for rotating API keys used in CloudFront distributions. It leverages [AWS Lambda](https://aws.amazon.com/lambda/) and [Secrets Manager](https://aws.amazon.com/secrets-manager/) to securely generate, test, and update API keys without manual intervention.

## Why API Key Rotation is Necessary

1. **Limit Exposure**: Regular rotation limits the time an API key is valid, reducing the window of opportunity for potential attackers.
2. **Compliance**: Many security standards and compliance frameworks require periodic rotation of secrets.
3. **Mitigate Risk**: If a key is compromised, rotation ensures it becomes invalid quickly.

## How It Works

The automated rotation process consists of four main steps:

1. **Create Secret**: Generate a new API key and store it as the "AWSPENDING" version in Secrets Manager.
2. **Set Secret**: Update the CloudFront distribution with the new API key.
3. **Test Secret**: Verify that the new API key works by testing it against the origin.
4. **Finish Secret**: Mark the new API key as "AWSCURRENT" in Secrets Manager, completing the rotation.

## Components

1. `exceptions.py`: Defines custom exceptions for the rotation process.
2. `utils.py`: Contains utility functions for interacting with CloudFront, Secrets Manager, and performing key rotation steps.
3. `handler.py`: Implements the Lambda function handler that orchestrates the rotation process.

## Usage

### Prerequisites

- Python 3.10+
- AWS account with appropriate permissions for Lambda, CloudFront, and Secrets Manager
- CloudFront distribution configured with a custom origin header for API key

### Setup

1. Build and deploy a Lambda function that contains the `amazon-cloudfront-api-key-rotator` using your preferred method (e.g., AWS Console, CloudFormation, or Terraform). Function configuration:
    - Python version: 3.10+
    - Lambda handler: `api_key_rotator.handler.lambda_handler`
    - Environment Variables: See "Environment Variables" section below
    - Permissions: See "IAM Permissions" section below

2. Configure Secrets Manager to use this Lambda function for rotation.

### Environment Variables

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `CLOUDFRONT_DISTRIBUTION_ID` | ID of the CloudFront distribution to update | None (Required) |
| `HEADER_NAME` | Name of the custom header for the API key | "x-origin-verify" |
| `ORIGIN_URL` | URL of the origin (API Gateway) to test the rotated API key against | None (Required) |
| `SECRET_KEY_NAME` | Key name for storing the API key in Secrets Manager | "HTTP_API_KEY" |
| `SECRET_KEY_LENGTH` | Length of the generated API key | 32 |

### IAM Permissions

Ensure the Lambda function has the necessary permissions to:

1. Manage secrets in AWS Secrets Manager:
    - `secretsmanager:GetSecretValue`
    - `secretsmanager:PutSecretValue`
    - `secretsmanager:DescribeSecret`
    - `secretsmanager:UpdateSecretVersionStage`

2. Access and update CloudFront distributions:
    - `cloudfront:GetDistribution`
    - `cloudfront:GetDistributionConfig`
    - `cloudfront:UpdateDistribution`

### Basic Example

Here's a basic example of how to use the rotator in your AWS environment:

1. Create a secret in AWS Secrets Manager with the initial API key:

   ```json
   {
     "HTTP_API_KEY": "your-initial-api-key"
   }
   ```

2. Configure the secret to use the Lambda function for rotation.

3. Update your CloudFront distribution to use the custom header (e.g., "x-origin-verify") with the current API key value.

4. The rotation will occur automatically based on the rotation schedule you set in Secrets Manager.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This software product is not affiliated with, endorsed by, or sponsored by Amazon Web Services (AWS) or Amazon.com, Inc. The use of the term "AWS" is solely for descriptive purposes to indicate that the software is compatible with AWS services. Amazon Web Services and AWS are trademarks of Amazon.com, Inc. or its affiliates.