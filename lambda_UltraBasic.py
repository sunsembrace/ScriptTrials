

def lambda_handler(event, context):
    name = event.get("name", "world")
    message = f"Hello {name}"

    print(message)
    
    return{
        "message": message
    }
