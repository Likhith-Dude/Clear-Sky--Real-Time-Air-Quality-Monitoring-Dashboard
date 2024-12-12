import boto3
from decimal import Decimal
from datetime import datetime
import random

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('AirQualityData')

# Insert data
data_list = [
    {"id": "test123", "PM2.5": Decimal(150), "PM10": Decimal(100), "CO2": Decimal(500), "timestamp": "2024-12-05T10:00:00"},
    {"id": "test124", "PM2.5": Decimal(80), "PM10": Decimal(120), "CO2": Decimal(450), "timestamp": "2024-12-05T12:00:00"},
    {"id": "test125", "PM2.5": Decimal(95), "PM10": Decimal(150), "CO2": Decimal(600), "timestamp": "2024-12-05T13:00:00"},
    {"id": "test126", "PM2.5": Decimal(50), "PM10": Decimal(80), "CO2": Decimal(400), "timestamp": "2024-12-05T14:00:00"},
    {"id": "test127", "PM2.5": Decimal(200), "PM10": Decimal(300), "CO2": Decimal(700), "timestamp": "2024-12-05T15:00:00"}
]

for data in data_list:
    table.put_item(Item=data)
    print(f"Inserted: {data}")