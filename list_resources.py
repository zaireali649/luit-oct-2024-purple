"""Script to list AWS resources."""
from helpers import *  # Assuming the required functions are in this module.


def print_bucket_names(s3_client: object) -> None:
    """Prints the names of all S3 buckets associated with the provided S3 client.

    Args:
        s3_client (object): The S3 client used to list and access S3 buckets.
    """
    bucket_names = list_buckets(s3_client)

    # Print elements of the list. Could also be done with '\n'.join(bucket_names)
    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client: object) -> None:
    """Prints the instance IDs of all EC2 instances associated with the provided EC2 client.

    Args:
        ec2_client (object): The EC2 client used to describe EC2 instances.
    """
    instances = describe_instances(ec2_client)

    instance_ids = []
    # Collect instance IDs. Could print instance['InstanceId'] directly to avoid this list.
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    # Print instance IDs. Could have printed directly in the loop above.
    for instance_id in instance_ids:
        print(instance_id)


# Initialize the clients
ec2_client = get_ec2_client()  # Retrieves the EC2 client for accessing EC2 resources
s3_client = get_s3_client()    # Retrieves the S3 client for accessing S3 resources

# Execute the functions
print_bucket_names(s3_client)
print_instance_ids(ec2_client)
