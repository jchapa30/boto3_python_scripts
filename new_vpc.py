import boto3

# Initialize the Boto3 EC2 client
ec2_client = boto3.client('ec2')

# Define the VPC parameters
vpc_cidr_block = '10.0.0.0/16'
vpc_instance_tenancy = 'default'

try:
    # Create the VPC
    response = ec2_client.create_vpc(
        CidrBlock=vpc_cidr_block,
        InstanceTenancy=vpc_instance_tenancy
    )
    vpc_id = response['Vpc']['VpcId']
    print(f"VPC with ID '{vpc_id}' created successfully!")

    # Add a tag to the VPC
    ec2_client.create_tags(
        Resources=[vpc_id],
        Tags=[
            {'Key': 'Name', 'Value': 'MyVPC'}
        ]
    )
    print("VPC tagged with name 'MyVPC'")
except Exception as e:
    print(f"An error occurred: {e}")
