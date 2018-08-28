import json
import boto3


def handle(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('sls_sample_db')

    body = json.loads(event['body'])
    print(body)

    result = table.put_item(
        Item={
            'id': body['id'],
            'fastname': body['fastname'],
            'lastname': body['lastname']
        }
    )

    response = {
        'statusCode': 200,
        'body': result
    }

    return response
