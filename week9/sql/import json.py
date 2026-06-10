import json
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


def create_users(name):
    if not os.path.exists("users.json"):
        with open("users.json","w",encoding="utf-8")as f:
            json.dump(name,f)
    else:
        with open("users.json","a",encoding="utf-8")as f:
            json.dump(name,f)

    