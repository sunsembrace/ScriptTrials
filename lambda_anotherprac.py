import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler (event, context):
    message = event.get("message")
    priority = event.get("priority","medium")