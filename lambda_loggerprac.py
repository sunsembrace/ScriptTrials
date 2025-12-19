import boto3

def lambda_handler(event, context):
    a = event.get("a",0)
    b = event.get("b", 0)

    #Validating input practice
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        print(f"Invalid inputs: a={a}, b={b}")
        return {"error": "Both a and b must be numbers."}
    
    result = a + b 
    print(f"Adding {a} + {b} gives us {result}")
    return {"result": result}