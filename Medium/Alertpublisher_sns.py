import json
import logging
import os
import boto3

#Logger set up.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#SNS Client
sns = boto3.client("s3")

#environment variable
ALERT_TOPIC_ARN = os.environ.get("ALERT_TOPIC_ARN")

def lambda_handler(event,context):
    try: 
        #extract fields
        alert_id = event.get("alert_id")
        service = event.get("service")
        severity = event.get("severity")
        message = event.get("message")

        #validate inputs early
        if not isinstance(alert_id,str) or not alert_id:
            logger.error("Invalid alert_id")
            return {"status": "error", "message": "Invalid alert_id"}
        
        if severity not in ("LOW", "MEDIUM", "HIGH"):
            logger.error("Invalid severity")
            return {"status": "error", "message": "Invalid severity"}
        
        if severity != "HIGH":
            logger.info(f"Alert {alert_id} ignored (serverity={severity})")
            return {"status": "ignored"}
        
        #build sns message
        sns_message = {
            "alert_id": alert_id,
            "service": service,
            "severity": severity,
            "message": message
        }

        #Publish to sns (fanout)
        sns.publish(
            TopicArn=ALERT_TOPIC_ARN,
            Message=json.dumps(sns_message),
            Subject=f"HIGH ALERT: {service}"
        )

        logger.info(f"Alert {alert_id} published to SNS")

        return {
            "status":"success",
            "alert_id": alert_id
        }

    except Exception as e:
        logger.error(f"Failed to publish alert: {str(e)}", exc_info= True)
        return {
            "status": "error",
            "message": "Internal server error"
        }