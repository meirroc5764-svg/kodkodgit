from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/calc/{a}/{op}/{b}")
def get_operator(op, a, b):
    '''returns operation and result calculated_value. Both a and b should be integers.
        Attention to div by zero'''
    if op == "add":
        return {"operation": op, "result": a + b}
    
    if op == "sub":
        return {"operation": op, "result": a - b}
    
    if op == "mul":
        return {"operation": op, "result": a * b}
    
    if op == "div":
        if a == 0 or b == 0:
            raise ZeroDivisionError("not div by zero")
        return {"operation": op, "result": a / b}

if __name__ == "__main__":
    uvicorn.run("server02:app", host="127.0.0.1", port=8000, reload=True)
