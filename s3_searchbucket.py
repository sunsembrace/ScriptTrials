import boto3

s3 = boto3.client("s3")

bucket_name = "Bucket_test1"

try:
    s3.head_bucket(Bucket=bucket_name)
    print("Bucket exists")
except:
    print("bucket does not exist!")