import boto3
import os

client = boto3.client('s3')

bucket_name=os.environ['bucket_name']

def lambda_handler(event, context):
    print ('into the function')
    all_objects=client.list_objects(Bucket=bucket_name)
    object_list=[]
    for each_obj in all_objects['Contents']:
        object_list.append(each_obj['Key'])
    print (object_list)