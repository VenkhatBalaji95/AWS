import boto3
import os

targetbucket = os.environ['target_bucket']
client = boto3.client('s3')

def lambda_handler(event, context):
    print ('into the function')
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    print (source_bucket)
    object_key = event['Records'][0]['s3']['object']['key']
    print (object_key)
    copy_source = {'Bucket': source_bucket, 'Key': object_key}
    target_bucket =targetbucket
    waiter = client.get_waiter('object_exists')
    wait = waiter.wait (Bucket = source_bucket,Key = object_key)
    copy_object = client.copy_object(Bucket = target_bucket, Key = object_key, CopySource = copy_source)