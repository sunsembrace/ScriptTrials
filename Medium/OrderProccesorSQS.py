import json
import logging
import os
import boto3
from botocore.exceptions import ClientError

# Logger setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS resources
dynamodb = boto3.resource("dynamodb")
ORDERS_TABLE = os.environ.get("ORDERS_TABLE")
table = dynamodb.Table(ORDERS_TABLE)


def lambda_handler(event, context):
    processed = 0
    failed = 0

    for record in event.get("Records", []):
        try:
            # 1. Parse SQS message body
            body = json.loads(record["body"])

            order_id = body.get("order_id")
            user_id = body.get("user_id")
            amount = body.get("amount")

 