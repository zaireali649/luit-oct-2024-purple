import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    response = s3.list_buckets()
    
    buckets = response['Buckets']
    
    bucket_names = []
    
    for bucket in buckets:
        print(bucket['Name'])
        bucket_names.append(bucket['Name'])
        
    # TODO implement
    return {
        'statusCode': 200,
        'body': '\n'.join(bucket_names)
    }
