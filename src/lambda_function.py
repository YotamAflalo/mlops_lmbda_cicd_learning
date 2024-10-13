import json

def lambda_handler(event, context):
    # TODO implement
    print("chacking cicd")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda CICD example repo!')
    }
