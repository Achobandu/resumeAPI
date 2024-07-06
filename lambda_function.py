import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('resumeChallenge')

def lambda_handler(event, context):
    try:
        # Scan the table to get all items
        response = table.scan()
        items = response['Items']
        
        # Handle pagination if there are more items
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])
        
          # Format the JSON with indentation and sorted keys
        formatted_json = json.dumps(items, indent=2, sort_keys=True)
        
        return {
            'statusCode': 200,
            'body': formatted_json,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # For CORS support
            }
        }
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Could not retrieve resume data'}, indent=2),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # For CORS support
            }
        }
