#First we want to import logger to make it easier to monitor errors and successes of our operations and the whys.
#Then we want to create a function named lambda_handler as we'll be ingesting data (events) and we'll use the event.get to do this under our variables.
#We then want to validate that the username x pw are of the correct datatypes and fit our criteria of not being empty.
#We then log this.
#We also then return it.

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    username = event.get("username")
    password = event.get("password")

    if not isinstance(username,("string") or not (password,("string"))):
        logger.error("Invalid datatype (is not a string) and is empty")
        return {
            "Error": f"Your {username} and/or {password} were not a string or were empty.
        }

    logger.info(f"{username}logged in successfully")
    
        return {
            "status": "success",
            "message": f"{username} logged in successfully!"
        }