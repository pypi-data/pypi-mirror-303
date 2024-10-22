# Secure Authorizer for Amazon API Gateway

This is a Lambda authorizer for [Amazon API Gateway](https://aws.amazon.com/api-gateway/) that provides secure API key validation using [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). This authorizer is compatible with [key rotation](https://github.com/efficient-solutions/amazon-cloudfront-api-key-rotator) through AWS Secrets Manager versioning, implements constant-time comparison to prevent timing attacks, and includes comprehensive logging for security monitoring.

## Features

- **AWS Secrets Manager Integration**: Securely retrieves API keys using AWS Secrets Manager
- **Key Rotation Compatibility**: Validates requests against both current and pending secret versions
- **Timing Attack Prevention**: Uses constant-time comparison for secure string matching
- **Comprehensive Logging**: Detailed logging for security monitoring and troubleshooting

## Installation

```bash
pip install amazon-api-gateway-secure-authorizer
```

## Configuration

### Environment Variables

- `SECRET_NAME`: The name or ARN of the secret in AWS Secrets Manager
- `SECRET_KEY_NAME`: The key name within the secret's JSON structure that contains the API key
- `HEADER_NAME`: (Optional) The name of the header containing the API key (default: "x-origin-verify")

### AWS Secrets Manager Setup

1. Create a new secret in AWS Secrets Manager with the following JSON structure:
```json
{
    "your_key_name": "your-api-key-value"
}
```

2. Ensure your Lambda function has the following IAM permissions:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": "arn:aws:secretsmanager:region:account-id:secret:secret-name"
        }
    ]
}
```

## Usage

### Lambda Handler

The Lambda function handler is located at:
```plaintext
secure_authorizer.authorizer.handler
```

### Example Event

```json
{
    "headers": {
        "x-origin-verify": "your-api-key-value"
    }
}
```

### Deployment Steps

1. **Set up AWS Secrets Manager**:
   - Create a new secret with your API key
   - Note the secret name and key name for environment variables

2. **Configure Lambda Environment**:
   ```bash
   SECRET_NAME="your-secret-name"
   SECRET_KEY_NAME="your-key-name"
   HEADER_NAME="x-origin-verify"  # Optional, this is the default
   ```

3. **Deploy Lambda Function**:
   - Set handler to `secure_authorizer.authorizer.handler`
   - Configure IAM role with necessary Secrets Manager permissions
   - Set memory and timeout appropriately (see Performance Recommendations)

4. **Configure API Gateway**:
   - Create a Lambda authorizer
   - Link it to your Lambda function
   - Configure authorization caching (see Performance Recommendations)

### Key Rotation

This authorizer supports seamless [key rotation](https://github.com/efficient-solutions/amazon-cloudfront-api-key-rotator) using AWS Secrets Manager's versioning:

1. Create a new version of your secret in AWS Secrets Manager
2. The new version will be automatically available as 'AWSPENDING'
3. The authorizer will accept both current and pending versions during rotation
4. Once rotation is complete, the new version becomes 'AWSCURRENT'

## Performance Recommendations

- **Memory**: 512MB
- **Timeout**: 5 seconds
- **Architecture**: ARM64
- **Authorization Caching**: 300-3600 seconds based on your security requirements

## Security Features

- **Secure Secret Storage**: Utilizes AWS Secrets Manager for encrypted key storage
- **Key Rotation Support**: Enables zero-downtime key rotation
- **Constant-time Comparison**: Prevents timing attacks during API key validation
- **Detailed Security Logging**: Helps identify potential security issues

## Error Handling

The authorizer implements comprehensive error handling for various scenarios:

- Missing environment variables
- Invalid or missing headers
- Secrets Manager access issues
- JSON parsing errors
- API key validation failures

All errors are logged with appropriate detail levels while maintaining security.

## Logging

The authorizer provides detailed logging at different levels:

- INFO: Successful authorizations
- WARNING: Failed authorizations
- ERROR: Configuration issues, Secrets Manager errors
- DEBUG: Additional validation details

## Comparison with [Simple Authorizer](https://github.com/efficient-solutions/amazon-api-gateway-simple-authorizer)

Advantages over the simple authorizer:

- Secure secret storage in AWS Secrets Manager
- Support for key rotation

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This software product is not affiliated with, endorsed by, or sponsored by Amazon Web Services (AWS) or Amazon.com, Inc. The use of the term "AWS" is solely for descriptive purposes to indicate that the software is compatible with AWS services. Amazon Web Services and AWS are trademarks of Amazon.com, Inc. or its affiliates.