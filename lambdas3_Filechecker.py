def lambda_handler(event, context):
    """
    AWS Lambda function triggered by an S3 event.
    Logs information about uploaded files and skips non-.txt files.
    """

    # Get the first record from the S3 event
    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]  # Bucket name where the file was uploaded
    key = record["s3"]["object"]["key"]      # File key (path) inside the bucket

    # Check if the uploaded file is a text file
    if key.endswith(".txt"):
        print(f"Received file: {key}")
        status = f"Processed {key}"
    else:
        print(f"Skipping non-text file: {key}")
        status = f"Skipped {key}"

    # Return a simple status message
    return {
        "status": status
    }
