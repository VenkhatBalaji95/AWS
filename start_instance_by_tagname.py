import boto3
import os

ec2 = boto3.resource('ec2')
instance_name = os.environ['instance_name']

def lambda_handler(event, context):
    print ('Enters into the function')
    instances = ec2.instances.filter(
    Filters=[{'Name': 'tag:Name', 'Values': [instance_name]}]).stop()