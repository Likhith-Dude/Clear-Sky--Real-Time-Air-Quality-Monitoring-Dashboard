import boto3
import csv
from decimal import Decimal

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('AirQualityData')

# Query for items where PM2.5 > 100
print("Querying for items where PM2.5 > 100...")
response = table.scan(
    FilterExpression="#pm25 > :value",
    ExpressionAttributeNames={"#pm25": "PM2.5"},
    ExpressionAttributeValues={":value": Decimal(100)}
)

items = response['Items']

# Export to CSV
if items:
    with open('query_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'PM2.5', 'PM10', 'CO2', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)
    print("Results saved to query_results.csv")
else:
    print("No items match the query condition. Nothing to export.")