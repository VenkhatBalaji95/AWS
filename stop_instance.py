import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    print ('Enters into the function')
    client.stop_instances(
    InstanceIds=[
        'i-0254259a85dae88fb'
    ])