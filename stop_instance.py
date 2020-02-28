import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    print ('Enters into the function')
    client.stop_instances(
    InstanceIds=[
        'pass the instance id'
    ])