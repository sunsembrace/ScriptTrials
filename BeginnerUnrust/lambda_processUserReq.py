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
    action = event.get("action")

#validate username
    if not isinstance(username,(str)) or not username:
        logger.error(f"Invalid username {username}: Must be a non empty string")
        return {
            "error": "Username must be a non-empty string"
        }

#Validate action
    if action not in ["login", "logout"]:
        logger.error(f"Invalid action: {action}")
        return {
            "error": "The action must be log in, or log out."
        }

    logger.info(f"{username} did {action}")
    return{
        "Success": f"user {username} was able to {action} successfully!"
    }