from fastapi import FastAPI
import uvicorn
#1)
app = FastAPI()

@app.get("/ping")
def get_pind():
    '''Returns servsr status'''
    return {"status": "pong"}

@app.get("/greeet/{name}")
def get_greet():
    '''Returns a greeting message with the given name'''
    return {"message": "hello {name}!"}

#2)
@app.get("/")
def get_api():
    '''Returns a message servers api and version'''
    return {"service": "my-api", "version":"1.0"}



@app.get("/users/admin")
def get_admin():
    '''returns dict {"role": "admin", "access": "full"}'''
    return {"role": "admin", "access": "full"}


@app.get("/user/{user_id}")
def get_email(user_id):
    "returns a hardcoded dict with user_id, name, email"
    return {"user_id":{user_id},
            "name":"meir",
            "email":"meirroc5764@gmail.com"}

if __name__ == "__main__":
    uvicorn.run("server01:app", host="127.0.0.1", port=8000, reload=True)
