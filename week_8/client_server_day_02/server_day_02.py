from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/greet")
def get_greet(name="word"):
    return{"message":f"hello,{name}!"}

if __name__ == ("__main__"):
    uvicorn.run("server_day_02:app",reload=True)
    get_greet("meir")