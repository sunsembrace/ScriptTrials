import json
import logging
import os
import boto3

#Logger set up.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#SNS Client
sns = boto3.client("s3")

#environment variable
ALERT_TOPIC_ARN = os.environ.get("ALERT_TOPIC_ARN")

def lambda_handler(event,context):
    try: 

    except Exception as e: