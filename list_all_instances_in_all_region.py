import boto3
import os

region = os.environ['region']
session=boto3.Session(region_name=region)

ec2 = session.resource('ec2')
ec2_client = session.client('ec2')

regions_list = []

#list all instances in one region
def lambda_handler(event, context):
    instances= ec2.instances.all()
    for each_instance in instances:
        print (each_instance.id, each_instance.state['Name'])
    list_all_regions()

#list all instances in all region
def list_all_regions():
    print ('Into all regions list')
    all_regions = ec2_client.describe_regions()
    for region in all_regions['Regions']:
        regions_list.append(region['RegionName'])
    list_instance_per_region()
    
def list_instance_per_region():
    print ('Into instances list per region')
    for region in regions_list:
        sessions=boto3.Session(region_name=region)
        ec2 = sessions.resource('ec2')
        for each_instance in ec2.instances.all():
            print (each_instance.id, each_instance.state['Name'])