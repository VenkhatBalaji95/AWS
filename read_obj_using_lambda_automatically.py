import boto3

client = boto3.client('s3')

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