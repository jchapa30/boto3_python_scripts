import boto3
import json
import datetime
import random

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_url = 'https://sqs.us-east-1.amazonaws.com/619007277676/customer_orders'

    # generate a message body containing the current time or a random number
    message_body = {
        'timestamp': str(datetime.datetime.now()),
        'random_number': random.randint(1, 100)
    }

    # send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message_body)
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to SQS queue')
    }
