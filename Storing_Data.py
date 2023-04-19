import boto3

sess = boto3.Session(region_name = "us-east-1")
s3client = sess.client("s3")

bucket_name = "joeychapa3030"


s3client.put_object(Bucket=bucket_name,Key ="test.txt", Body =b"Hello")
