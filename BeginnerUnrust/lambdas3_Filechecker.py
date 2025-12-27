import boto3

def lambda_handler(event, context):
    record = event["Records"][0] #Check first file event.
    bucket = record["s3"]["bucket"]["name"] #Bucket name
    file_name = record["s3"]["bucket"]["key"] #Check for file name

    if file_name.endswith(".txt"): #Extract by condition .txt
        s3 = boto3.client("s3") #Connect to aws sdk
        response = s3.get_object(Bucket=bucket, Key=file_name) #client response
        text = response["body"].read().decode("utf-8")
        line_count = len(text.splitlines())

        print(f"Received file: {file_name}")
        print(f"Line count: {line_count}")

        return {"file": file_name, "lines": line_count}
    
    else:
        print(f"Skipping non-txt files {file_name}")
        return {"status": "skipped"}
