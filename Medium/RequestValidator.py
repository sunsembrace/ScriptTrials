import boto3
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Import API  gateway, then lambda via lambda handler.
#import Logging, Import boto3, import JSON since json format
#Take in input
# Validate input
#Return 200, 400.
#Log throughout whenever we return or come into errors.

api_gw = boto3.client('apigateway')

def lambda_handler(event,context):
    try:
        name = event.get('name')
        age = event.get('age')

        if not isinstance(name,str) or not name:
            logger.error("400": "Invalid name")
            return {"Status":"Failed", "message": "unable to find valid name"}

        if not isinstance(age,int) or not age:
            logger.error("400":"Invalid name")
            return {"status": "Failed", "message": "unable to find valid age"}
            
    #Validate it into AWS service.
    #Feel like this is wrong and we weremeant to do it benfore hand.

    except Exception as e:
        logger.error
        return 