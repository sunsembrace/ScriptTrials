#1.Import Json
#2Import logging
#3Take in event via lambda handler.
#4Validate each step early using status codes such as 200,400.
#5Parse body.
#6Validate body.
#7 Extract specific fields (name, age)
#8 Validate specific events.
#9 sucess response via status code
#10 Ensure wrapped in try, except
#11 Double check.

import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    try:
        #Parse request body.
        body = event.get("body")

        if body is None:
            logger.error("Missing request for body")
            return {"StatusCode": 400,
                    "body": json.dumps({"error": "Request body is required"}) 
                    }
        
        data = json.loads(body)

        #2. Extract fields.
        name = data.get("name")
        age = data.get("age")

        if not isinstance(name,str) or not name:
            logger.error("Invalid name")
            return {"StatusCode": 400,
                    "Message": "Unable to get name"}
        
        if not isinstance(age,int) or not age:
            logger.error("Invalid age")
            return{"StatusCode": 400,
                   "Message": "Unable to get name"}

        #4Succcess response
        logger.info(f"Success. Validated request for {name} with {age}")
        return {"StatusCode": 200,
                "Body": json.dumps({
                    "message": f"Hello {name}, age {age} accepted."
                })}

    except Exception as e:
        logger.error(f"Unexpected error {str(e)}", exc_info=True)
        return {
            StatusCode: 500,
            "body": json.dumps({"error": "Internal server error"})
        }