import boto3

# Create a Boto3 S3 client
s3_client = boto3.client('s3')
# Create a Boto3 S3 resource
s3_resource = boto3.resource('s3')

# Define the name of the new bucket
new_bucket_name = 'my-dogs-bucket2024'

# Check if the bucket name is available
def check_bucket_exists(bucket_name):
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return bucket_name in buckets

if check_bucket_exists(new_bucket_name):
    print(f"The bucket '{new_bucket_name}' already exists.")
else:
    # Create the new S3 bucket
    s3_client.create_bucket(Bucket=new_bucket_name)
    print(f"Bucket '{new_bucket_name}' created successfully.")

# Write content to a file
with open("myfile.txt", "w") as file:
    file.write("This is a test file to upload.")

# Upload the file to the new S3 bucket
s3_resource.Object(new_bucket_name, 'test_upload_file').upload_file(Filename='myfile.txt')

print("File uploaded successfully.")
