import boto3

#connect to s3
s3_client = boto3.client("s3")
s3 = boto3.resource('s3')


#create bucket
# bucketName = "atrivedi89-bucket-1"
# s3_client.create_bucket(
#     Bucket = bucketName
    
#     )

#list buckets-client
response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(bucket)
    print(bucket["CreationDate"])

#list buckets-resource
for bucket in s3.buckets.all():
    print(bucket)

#upload file
#s3.Bucket(bucketName).upload_file('/tmp/hello.txt', 'hello.txt')

#delete object
#s3.Object(bucketName, 'hello.text').delete()

#delete bucket
# respsonse = s3_client.deleteBucket(
#     Bucket = bucketName
#     )

