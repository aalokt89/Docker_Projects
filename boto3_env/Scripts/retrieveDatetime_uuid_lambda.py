import boto3
import os
import json
from datetime import datetime

# environment variables
TOPIC_ARN = os.environ['TOPIC_ARN']
sns = boto3.client('sns')


def lambda_handler(event, context):
   # get message data from event
    messageData = event['Records'][0]
    message = {
        'message_id': messageData['messageId'],
        'body': messageData['body'],
        'timestamp': datetime.now().isoformat()
    }
    try:
        # publish message to sns
        response = sns.publish(
            TopicArn=TOPIC_ARN,
            Message=json.dumps(message, indent=4),
            Subject='DATETIIME_UUID_MESSAGE'
        )

        print(f"Message sent to sns: {json.dumps(message, indent=4)}")

    except Exception as e:
        print(e)

    return response
