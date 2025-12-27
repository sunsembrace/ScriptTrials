import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler (event, context):
    message = event.get("message")
    priority = event.get("priority","medium")

    #validate the message
    if not isinstance(message,str) or not message:
        logger.error("Invalid message: must be a non-empty string")
        return {
            "error": "Message must be a non-empty string"
        }
    
    #validate priority
    allowed_priorities = ["low", "medium","High"]
    if not isinstance(priority, str) or priority not in allowed_priorities:
        logger.errror(f"Invalid priority: {priority}")
        return {
            "Error": "Priority must be one of: low, medium, high"
        }
    
    #format message
    formatted_message = f"[{priority.upper()}] {message}"

    #log success
    logger.info(f"Formatted message created: {formatted_message}")

    #return response
    return {
        "status": "success:",
        "formatted message": formatted_message
        }
