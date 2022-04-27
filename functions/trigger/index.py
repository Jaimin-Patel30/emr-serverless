import boto3
import logging 

def lambda_handler(event, context):
    print(event)
    return event