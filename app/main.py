from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .utils import fib

app = FastAPI(title="Fibonacci API")

@app.get("/fib")
def get_fibonacci(n: int):
    if n < 0:
        return JSONResponse(status_code=400, content={"status_code": 400, "detail": "n must be non-negative"})
    return {"n": n, "result": fib(n)}
