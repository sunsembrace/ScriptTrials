import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

def lambda_handler(event,context):
    try:
        user_id = event.get("user_id")
        email = event.get("email")
        age = event.get ("age")

        if not isinstance(user_id,str) or not user_id:
            logger.error("Error: Invalid user_id")
            return {"status": "error", "message":"Invalid user_id"}

        if not isinstance(email,str) or not email:
            logger.error("Error: Invalid email")
            return {"status": "error", "message": "invalid email"}

        if not isinstance(age,str) or not age:
            logger.error("error: Invalid age")
            return {"status": "error", "message": "invalid age"}
            
        table.putitem(
        Item={
            "user_id": user_id,
            "email": email,
            "age": age

        }
        )
        logger.info(f"User {user_id} created successfully.")

        return {
            "status": "success",
            "user_id": user_id,
            "email": email,
            "age": age
        }

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info = True)
    return {"status": "error", "message": "Internal server error"}