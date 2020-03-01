import boto3
import os

client = boto3.client('s3')

bucket_name=os.environ['bucket_name']
object_name = os.environ['object']

def lambda_handler(event, context):
    print ('into the function')
    obj = client.get_object(Bucket=bucket_name,Key=object_name)
    read_obj= obj['Body'].read().decode('utf-8')
    print (read_obj)