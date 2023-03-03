import boto3
from pprint import pprint
import time

ec2 = boto3.client('ec2', region_name='us-east-1')


def stopInstanceByTag(key, value):
    # get instances by tag and value
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:'+key,
                'Values': [value]
            }
        ]
    )

    # stop selected instances if state == running
    for each in response['Reservations']:
        for instance in each['Instances']:

            if instance['State']['Name'] == 'running':
                ec2.stop_instances(InstanceIds=[instance['InstanceId']])

                return 0

            else:
                print(
                    f"The following instances are not running, and, therefore, cannot be stopped \n {instance['InstanceId']}")
                print(instance['State']['Name'])
                return 1


stopInstanceByTag('Environment', 'Dev')
