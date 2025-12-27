import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    a = event.get("a")
    b = event.get("b")
    operation = event.get("operation", "add")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        logger.error(f"Invalid inputs: a={a}, b={b}")
        return {
            "error": "Both inputs must be numbers"
        }

    if operation == "add":
        result = a + b
    elif operation == "multiply":
        result = a * b
    else:
        logger.error(f"Unsupported operation: {operation}")
        return {
            "error": "Unsupported operation. Use 'add' or 'multiply'."
        }

    logger.info(f"Operation {operation} completed successfully")

    return {
        "operation": operation,
        "result": result
    }

