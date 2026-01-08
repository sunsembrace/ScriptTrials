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
        
        #2. Extract fields
        user_id = data.get("user_id")
        email = data.get("email")

        #3. Validate the fields. 
        if not isinstance (user_id,str) or not user_id:
            logger.error("User_ID not found")
            return {"StatusCode": 400,
                    "body": json.dumps({"Error": "Invalid user ID"})
                    }
        
        if not isinstance (email,str) or "@" not in email:
            logger.error("Email not found")
            return {"StatusCode":400, 
                    "body": json.dumps({"Error":"Invalid email"})
                    }
        
        #4. Conditional writes to DynamoDB.
    
    except Exception as e:
        logger.error()