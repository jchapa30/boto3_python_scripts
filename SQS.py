import boto3

sqs_client = boto3.client("sqs", region_name = 'us-east-1')

sqs_client.create_queue(QueueName ='customer_orders')
  
