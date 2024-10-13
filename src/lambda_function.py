import json

def lambda_handler(event, context):
    # TODO implement
    #we added sns :) and fix it
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda CICD example repo!')
    }
