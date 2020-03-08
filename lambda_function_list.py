import boto3
import os

client = boto3.client ('lambda')
version = os.environ['version']
topic = os.environ['topic']
subject = os.environ['subject']

s3 = boto3.client('sns')

def lambda_handler(event, context):
    print ('into the function')
    function = client.list_functions(FunctionVersion='ALL')
    lambda_function = function['Functions']
    function_name = []
    for a in lambda_function:
        if a['Runtime'] == version:
            function_name.append(a['FunctionName'])
    print ('The old Lambda functions are:',function_name)
    if function_name:
        s3.publish(TopicArn=topic,Message=str(function_name),Subject=subject)