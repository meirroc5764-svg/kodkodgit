import uvicorn
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/status")
def get_status():
    '''returns a system information a corrent time  and a hardcoded server name'''
    return {"infomation": datetime.now(),"server_name":"app"}


if __name__ == "__main__":
    uvicorn.run("server03:app", host="127.0.0.1", port=8000, reload=True)
