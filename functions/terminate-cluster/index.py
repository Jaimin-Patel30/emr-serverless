import boto3
import logging 

def lambda_handler(event, context):
    Logger.info(event)
    return event