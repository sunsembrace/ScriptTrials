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

# Environment variable
USERS_TABLE = os.environ.get("USERS_TABLE")

# DynamoDB table reference
table = dynamodb.Table(USERS_TABLE)


def lambda_handler(event, context):
    try:
        # 1. Parse request body (API Gateway style)
        body = event.get("body")

        if body is None:
            logger.error("Missing request body")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Request body is required"})
            }

        data = json.loads(body)

        # 2. Extract fields
        user_id = data.get("user_id")
        email = data.get("email")

        # 3. Validate inputs (fail early)
        if not isinstance(user_id, str) or not user_id:
            logger.error("Invalid user_id")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid user_id"})
            }

        if not isinstance(email, str) or "@" not in email:
            logger.error("Invalid email")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid email"})
            }

        # 4. Conditional write to DynamoDB (prevent duplicates)
        table.put_item(
            Item={
                "user_id": user_id,
                "email": email
            },
            ConditionExpression="attribute_not_exists(user_id)"
        )

        logger.info(f"User {user_id} created successfully")

        # 5. Success response
        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "User created successfully",
                "user_id": user_id
            })
        }

    except ClientError as e:
        # Handle duplicate user specifically
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            logger.warning(f"Duplicate user attempt: {user_id}")
            return {
                "statusCode": 409,
                "body": json.dumps({"error": "User already exists"})
            }

        logger.error(f"DynamoDB error: {str(e)}", exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Database error"})
        }

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }
