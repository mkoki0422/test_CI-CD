import json

SLACK_API_TOKEN = os.environ.get('SLACK_API_TOKEN')

def lambda_handler(event, context):
    body = {
        "message": SLACK_API_TOKEN,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
.