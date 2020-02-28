import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    print ('Enters into the function')
    client.start_instances(
    InstanceIds=[
        'pass the instance id'
    ])