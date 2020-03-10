import boto3
import os

client = boto3.client ('s3')
dynamodb = boto3.resource('dynamodb')

bucket = os.environ['bucket_name']
key = os.environ['object_name']
table_name = os.environ['table_name']
table = dynamodb.Table(table_name)

column1=os.environ['column_1']
column2=os.environ['column_2']

def lambda_handler(event, context):
    file_object = client.get_object(Bucket=bucket, Key = key)
    obj = file_object['Body'].read().decode('utf-8').split()
    print ('The value present in .csv file is', obj)
    split_obj=[]
    for i in obj:
        a = i.split(',')
        split_obj.append(a)
    print ('The split object value is', split_obj)
    i=0
    list = []
    while i < len(split_obj):
        j=0
        set = {}
        set['Emp_id'] = split_obj[i][j]
        set['Emp_name'] = split_obj[i][j+1]
        list.append(set)
        i+=1
    print ('The final value is', list)

    for i in range(len(list)):
        value = list [i]
        print ('The employee ID is', value['Emp_id'])
        print ('The employee name is', value['Emp_name'])
        Emp_id=int(value['Emp_id'])
        
        table.put_item(Item=
        {column1:Emp_id,
        column2:value['Emp_name']})