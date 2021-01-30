import json
import boto3
region  = 'us-east-1'
ec2 = boto3.client('ec2',region_name = region)
def lambda_handler(event, context):
    '''
    Function to start stop aws ec2 instace
    '''
    instances = event['queryStringParameters']['instances']
    action = event['queryStringParameters']['action']
    if action == 'start':
        print('Starting Instances')
        ec2.start_instances(InstanceIds=[instances])
        response = "Succefully started instances"
    elif action =='stop':
        print('Stopping Instances')
        ec2.stop_instances(InstanceIds=[instances])
        response = "Succefully stopped instances"
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
