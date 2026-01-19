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

            # 2. Validate inputs
            if not isinstance(order_id, str) or not order_id:
                raise ValueError("Invalid order_id")
            if not isinstance(user_id, str) or not user_id:
                raise ValueError("Invalid user_id")
            if not isinstance(amount, (int, float)) or amount <= 0:
                raise ValueError("Invalid amount")

            # 3. Write to DynamoDB
            table.put_item(
                Item={
                    "order_id": order_id,
                    "user_id": user_id,
                    "amount": amount,
                    "status": "CREATED"
                }
            )

            logger.info(f"Processed order {order_id}")
            processed += 1

        except (ValueError, ClientError, json.JSONDecodeError) as e:
            logger.error(f"Failed to process record: {str(e)}", exc_info=True)
            failed += 1
            # Let SQS retry this message automatically

    return {
        "status": "complete",
        "processed": processed,
        "failed": failed
    }
