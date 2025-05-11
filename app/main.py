from fastapi import FastAPI, HTTPException
from .utils import fib

app = FastAPI(title="Fibonacci API")

@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be non-negative")
    return {"n": n, "fibonacci": fib(n)}
