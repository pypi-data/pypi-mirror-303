import boto3
import pandas as pd
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #authenticates with iam role
client = dynamodb.meta.client

def float_to_dec(value):
    if isinstance(value, float):
        return Decimal(value)
    return value

def import_to_dynamodb(file, table_name, primary_key):
    #check if table exists
    tables = client.list_tables()['TableNames']
    if table_name in tables:
        print(f"Table {table_name} already exists, inserting data now ...")
        table = dynamodb.Table(table_name)
    #create table
    else:
        try: 
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': primary_key,
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': primary_key,
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            )
            table.wait_until_exists()
            print(f"Table {table_name} created successfully")
        except Exception as e:
            print(f"Error creating table: {e}")
            return None
    
    #import rows into table 
    data = pd.read_csv(file)
    for _, row in data.iterrows():
        item = {k: float_to_dec(v) for k, v in row.to_dict().items()}
        try:
            table.put_item(Item=item)
        except Exception as e:
            print(f"Error importing data: {e}")
            return None
        
    print('Data has been imported to DynamoDB')



