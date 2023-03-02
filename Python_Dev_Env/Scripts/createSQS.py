import boto3

sqs = boto3.resource('sqs', region_name='us-east-1')


def createSQS(queueName):

    queue = sqs.create_queue(QueueName=queueName)
    queueURL = queue.url
    queueARN = queue.arn

    print(queueURL)
    print(queueARN)


createSQS('test-sqs2')

# print(sqs.get_queue_by_name(QueueName='DateTime_UUID_sqs').url)
