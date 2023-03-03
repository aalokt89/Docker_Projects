import boto3
from pprint import pprint


ec2_cl = boto3.client('ec2')
ec2_re = boto3.resource('ec2')

# instances = ec2_re.instances.all()

# resource
# for instance in instances:
#     print(f"resource: {instance.id}, {instance.state['Name']}")
#     print('--------------------')

# client
# for each in ec2_cl.describe_instances()['Reservations']:
#     for instance in each['Instances']:

#         instanceState = instance['State']['Name']
#         pprint(instance['Tags']['Environment'])

response = ec2_cl.describe_instances(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['Prod']
        }
    ]
)
resourceList = []

for each in response['Reservations']:
    for instance in each['Instances']:
        resourceList.append(instance['InstanceId'])

print(resourceList)
pprint(ec2_cl.stop_instances(InstanceIds=resourceList))

# repsonse = ec2_cl.describe_tags(
#     Filters=[
#         {
#             'Name': 'tag:Environment',
#             'Values': ['Dev']
#         }
#     ]
# )

# pprint(response)
