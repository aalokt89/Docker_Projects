import json
from datetime import datetime
import uuid
import os
import boto3

# set env variables
DATETIME = os.environ['GET_DATETIME']
UUID = os.environ['GET_UUID']
QUEUE_URL = os.environ['QUEUE_URL']


def lambda_handler(event, context):
    apiEvent = event['rawPath']
    sqs = boto3.resource('sqs')
    queue = sqs.Queue(QUEUE_URL)

    try:
        if apiEvent == DATETIME:
            message = datetime.strftime(
                datetime.now(), "%m-%d-%Y, %I:%M:%S %p (UTC)")

        elif apiEvent == UUID:
            message = str(uuid.uuid4())

        else:
            print(f"Error: '{apiEvent}' does not exist.")

        print(message)

        response = queue.send_message(MessageBody=message)

        print(f"MessageID: '{response['MessageId']}' sent to queue.")

        return json.dumps(message)

    except Exception as e:
        print(e)
