from helpers import *


def create_instances(client: 'boto3.client', ami_type: str, instance_amount: int = 1) -> None:
    """
    Creates EC2 instances based on the specified AMI type.

    Args:
        client (boto3.client): The EC2 client used to create instances.
        ami_type (str): The type of AMI to use for the instances (e.g., "ubuntu", "linux 2023", "linux 2").
        instance_amount (int, optional): The number of instances to create. Defaults to 1.

    Returns:
        None
    """

    # Loop through the number of instances to create
    for i in range(instance_amount):
        # Normalize ami_type by converting to lowercase and removing extra spaces
        ami = ami_type.lower().strip()

        # Check for Ubuntu AMI type
        if ami == "ubuntu":
            create_ubuntu_instance(client)  # Create Ubuntu instance
            print("Created Ubuntu Instance")

        # Check for Amazon Linux 2023 AMI type
        elif ami == "linux 2023":
            create_amazon_linux_2023_instance(client)  # Create Amazon Linux 2023 instance
            print("Created Linux 2023 Instance")

        # Check for Amazon Linux 2 AMI type
        elif ami == "linux 2":
            create_amazon_linux_2_instance(client)  # Create Amazon Linux 2 instance
            print("Created Linux 2 Instance")

        # Handle invalid AMI type
        else:
            print("Invalid AMI Type")


# Example usage of the function
ec2_client = get_ec2_client()
create_instances(ec2_client, "linux 2")
