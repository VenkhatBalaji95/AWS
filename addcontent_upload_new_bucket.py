import boto3
import os

client = boto3.client('s3')

new_bucket = os.environ['bucket_name']

def lambda_handler(event, context):
   print ('Into the function')
   
   if event:
       print ('Event is:', event)
       object = event['Records'][0]
       print ('Object is:', object)
       bucket_name = object ['s3']['bucket']['name']
       print ('Bucket name is:', bucket_name)
       file_name = object ['s3']['object']['key']
       print ('File name is:', file_name)
       
       file_object = client.get_object(Bucket=bucket_name, Key = file_name)
       obj = file_object['Body'].read().decode('utf-8')
       print ('Content present in file is :', obj)
       
       default_value = obj + ' THANKS FOR UPLOADING THE FILE INTO S3 BUCKET'
       print (default_value)
       print ('The updated content is:', default_value)
       client.put_object(Bucket= new_bucket, Key=file_name, Body = default_value)
       print ('update is successful')
       
       file_object = client.get_object(Bucket = new_bucket, Key = file_name)
       obj = file_object['Body'].read().decode('utf-8')
       print ('New Content present in file is :', obj)