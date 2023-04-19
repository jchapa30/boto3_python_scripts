import boto3


sess = boto3.Session(region_name = "us-east-1")
s3client = sess.client("s3")

bucket_name = "joeychapa3030"

s3objectlist = s3client.list_objects(Bucket=bucket_name)

for s3object in s3objectlist["Contents"]:
    print(s3object['Key'])