import boto3
from typing import Any, Dict


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler function to list all S3 bucket names.

    This function retrieves the names of all S3 buckets in the AWS account
    and returns them in the response body as a newline-separated string.

    Args:
        event (Dict[str, Any]): The event triggering the Lambda function.
        context (Any): Contextual information provided by AWS Lambda.

    Returns:
        Dict[str, Any]: A dictionary containing the HTTP status code and
        the body with bucket names as a newline-separated string.
    """
    # Initialize S3 client
    s3 = boto3.client('s3')

    # List all S3 buckets
    response = s3.list_buckets()

    # Extract bucket list from response
    buckets = response['Buckets']

    # Initialize list to store bucket names
    bucket_names = []

    # Iterate through each bucket and append its name to bucket_names list
    for bucket in buckets:
        print(bucket['Name'])  # Log each bucket name for debugging
        bucket_names.append(bucket['Name'])

    # Return the response with status code and joined bucket names
    return {
        'statusCode': 200,
        'body': '\n'.join(bucket_names)
    }
