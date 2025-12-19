import boto3

def lambda_handler(event, context):
    a = event.get("a",0)
    b = event.get("b", 0)

    result = a + b 

    print(f"Adding {a} + {b} gives us {result}")

    return {"result": result}