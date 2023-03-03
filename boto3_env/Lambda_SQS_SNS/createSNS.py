import boto3

sns = boto3.resource('sns', region_name='us-east-1')

def createSNS(topicName):
    try:
        topic = sns.create_topic(Name=topicName)
        print(topic.arn)

    except Exception as e:
        print(e)


# createSNS('datetime-uuid-topic')

topics = sns.topics.all()
for topic in topics:
    if 'dateTime-uuid-topic' in topic.arn:
        print(topic.arn)
