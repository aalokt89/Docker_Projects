import boto3
from pprint import pprint

ec2 = boto3.client('ec2', region_name='us-east-1')


def stopInstanceByTag(key, value):
    successList = []
    failList = []

    # get instances by tag and value
    response = ec2.describe_instances(Filters=[ {'Name': 'tag:'+key, 'Values': [value]} ])

    # stop selected instances if state == running
    for each in response['Reservations']:
        for instance in each['Instances']: #iterate over reservations to get instance info

            if instance['State']['Name'] == 'running': #stop instances if they are currently running
                ec2.stop_instances(InstanceIds=[instance['InstanceId']])
                #store stopped instance ids for later feedback display
                successList.append({ 
                    'instanceId': instance['InstanceId'],
                    'State': instance['State']['Name']
                })
            else:
                failList.append(instance['InstanceId'])

    # print out successfully stopped instances
    print("----------------------")
    print("The following instances have been stopped:")
    print(successList)
    print("----------------------")

#call function to execute
stopInstanceByTag('Environment', 'Dev')
