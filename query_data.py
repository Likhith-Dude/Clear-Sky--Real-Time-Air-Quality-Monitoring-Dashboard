import boto3
from decimal import Decimal

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('AirQualityData')

# Fetch all items
print("Fetching all items...")
response = table.scan()
for item in response['Items']:
    print(item)

# Query for items where PM2.5 > 100
print("\nQuerying for items where PM2.5 > 100...")
try:
    response = table.scan(
        FilterExpression="#pm25 > :value",
        ExpressionAttributeNames={"#pm25": "PM2.5"},
        ExpressionAttributeValues={":value": Decimal(100)}
    )
    items = response['Items']
    if items:
        print("Items matching the query condition:")
        for item in items:
            print(item)
    else:
        print("No items match the query condition.")
except Exception as e:
    print(f"Error occurred: {e}")