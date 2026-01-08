#Import Json
#Import Logging
#Import boto3
#Take in event
#Extract fields such as name from the event.
#Compare it against a database
#IF not currently existing, then creation can occur.
#Otherwise reject
#Validate throughout.

import json
import os
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DynamoDB = boto3.resources("DynamoDB")

#ENV variable.
USERS_TABLE = os.environ.get("USERS_TABLE")

#DynamoDB reference table.
table = DynamoDB.Table( USERS_TABLE)


def lambda_handler(event,context):
    try:
        #1. Take in event
        body = event.get("body")

        if body is None:
            logger.error("Missing Body request")
            return {"StatusCode": 400,
                    "body": json.dumps ({"error": "Request body is required"})
                    }
        
        data = json.loads(body)
        
        
    
    except Exception as e:
        logger.error()