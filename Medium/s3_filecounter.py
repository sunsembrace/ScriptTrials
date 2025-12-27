#Task - s3 File line Counter with Summary Output
 #   We recieve text files in an s3 bucket.
  #  For each file uploaded, we want to count how many lines it has and store a summary.

#Plan.
#1. Create a lambda which responds to the s3 ingesting txt files only. (so input from an event).
#2. Take that file and count how many lines it has.
#3. We then store it as a summary output maybe into a new s3 bucket.

#Better plan
#Lambda trigger by an S3 ObjectCreated event. (input from event is bucket x key)
#1. Only process files that end in .txt
#2. Are uploaded under /incoming.
#3. Read the file from s3
#4. Count how many lines in the txt file.
#5. Write a summary JSON file to: Processed/filename.summary.json
#6. Log txt file name, line count, where summary written.

import boto3
import logging
import json

logger = logging.getLogger()
logger.setlevel(logging.INFO)

s3 = boto3.client("s3")

import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")

def lambda_handler(event, context):
    try:
        # 1. Extract S3 info from the event
        record = event["Records"][0]
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        logger.info(f"Received file: s3://{bucket}/{key}")

        # 2. Validate file path and extension
        if not key.startswith("incoming/") or not key.endswith(".txt"):
            logger.info("File does not meet processing criteria. Skipping.")
            return {"status": "skipped"}

        # 3. Read file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        file_content = response["Body"].read().decode("utf-8")

        # 4. Count lines
        line_count = len(file_content.splitlines())

        logger.info(f"Line count for {key}: {line_count}")

        # 5. Prepare summary
        filename = key.split("/")[-1]
        summary = {
            "filename": filename,
            "line_count": line_count
        }

        summary_key = f"processed/{filename}.summary.json"

        # 6. Write summary back to S3
        s3.put_object(
            Bucket=bucket,
            Key=summary_key,
            Body=json.dumps(summary),
            ContentType="application/json"
        )

        logger.info(f"Summary written to s3://{bucket}/{summary_key}")

        return {
            "status": "success",
            "summary_key": summary_key
        }

    except Exception as e:
        logger.error(f"Processing failed: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "message": str(e)
        }

