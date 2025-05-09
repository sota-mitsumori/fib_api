import json
from app.utils import fib

def handler(request, n):
    try:
        n_int = int(n)
    except ValueError:
        return {"statusCode": 400, "body": json.dumps({"detail": "n must be an integer"})}

    if n_int < 0:
        return {"statusCode": 400, "body": json.dumps({"detail": "n must be non-negative"})}

    result = fib(n_int)
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"n": n_int, "fibonacci": result})
    }
