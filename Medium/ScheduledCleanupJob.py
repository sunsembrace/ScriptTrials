import logging
import time
import os
import boto3

#Logger setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#AWS Resources
dynamodb = boto3.resource("dynamodb")

#environment variable
SESSION_TABLE = os.environ.get("SESSION_TABLE")

def lambda_handler(event,context):
    #1. Get current time
    current_time = int(time.time())
    logger.info(f"Cleanup started at {current_time}")

    #2. Scan DynamoDB for expired sessions
    response = table.scan(
        FilterExpressions ="expires at < : now",
        ExpressionAttributeValues= {
            ":now": current_time
        }
    )

    expired_sessions = response.get("Items",[])
    logger.info(f"Found {len(expired_sessions)} expired sessions")

    #3. Delete expired sessions
    deleted_count = 0

    for sessions in expired_sessions:
        session_id = sessions["session id"]
        