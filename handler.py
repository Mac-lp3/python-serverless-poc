import json
from payload_handler import PayloadHandler

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
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

def payload(event, context):
    payload = {}
    payload['operation'] = 'create'
    payload['body'] = 'heres the body'
    handler = PayloadHandler({'key': 'value'})
    handler.beginProcessing(payload)
