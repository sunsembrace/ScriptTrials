import json
import logging
import os
import boto3

# Logger setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS clients/resources
dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

# Environment variables (configuration)
ORDERS_TABLE = os.environ.get("ORDERS_TABLE")
ORDER_TOPIC_ARN = os.environ.get("ORDER_TOPIC_ARN")

# DynamoDB table reference
table = dynamodb.Table(ORDERS_TABLE)


def lambda_handler(event, context):
    try:
        # 1. Extract inputs
        order_id = event.get("order_id")
        user_id = event.get("user_id")
        amount = event.get("amount")

        # 2. Validate inputs (fail early)
        if not isinstance(order_id, str) or not order_id:
            logger.error("Invalid order_id")
            return {"status": "error", "message": "Invalid order_id"}

        if not isinstance(user_id, str) or not user_id:
            logger.error("Invalid user_id")
            return {"status": "error", "message": "Invalid user_id"}

        if not isinstance(amount, (int, float)) or amount <= 0:
            logger.error("Invalid amount")
            return {"status": "error", "message": "Invalid amount"}

        # 3. Write order to DynamoDB
        table.put_item(
            Item={
                "order_id": order_id,
                "user_id": user_id,
                "amount": amount,
                "status": "CREATED"
            }
        )

        logger.info(f"Order {order_id} stored in DynamoDB")

        # 4. Publish notification to SNS
        message = {
            "order_id": order_id,
            "user_id": user_id,
            "amount": amount,
            "status": "CREATED"
        }

        sns.publish(
            TopicArn=ORDER_TOPIC_ARN,
            Message=json.dumps(message),
            Subject="New Order Created"
        )

        logger.info(f"Notification sent for order {order_id}")

        # 5. Return success
        return {
            "status": "success",
            "order_id": order_id
        }

    except Exception as e:
        logger.error(f"Processing failed: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "message": "Internal server error"
        }
