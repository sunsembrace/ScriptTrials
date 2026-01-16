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