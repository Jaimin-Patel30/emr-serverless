import boto3
import logging 

def lambda_handler(event, context):
    logging.info(event)
    return event