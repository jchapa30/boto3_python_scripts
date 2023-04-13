import boto3

dynamodb = boto3.resource('dynamodb')
table_name = "Mascots"
table = dynamodb.Table(table_name)
table.delete()

print(f"Table '{table_name}' has been deleted successfully.")"""
Your module description
"""
