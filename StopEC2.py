import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    instance_ids = ['i-0c0ead114f199caa2', 'i-08c38e92d3bddf523']
    ec2.start_instances(InstanceIds=instance_ids)
    print('Started instances: ' + str(instance_ids))
