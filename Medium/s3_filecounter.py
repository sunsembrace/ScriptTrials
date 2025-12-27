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

def lambda_handler(event,context):
    s3 = boto3.client("s3")
    bucket = 

