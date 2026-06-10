from fastapi import FastAPI, HTTPException
import uvicorn

from database_manager import *
from reports import *


app = FastAPI()

@app.get("/",status_code=200)
def get_to_base():
    if not all_data:
        raise HTTPException(status_code=404,detail="no have data")
    return all_data()

@app.put("/new",status_code=200)
def creat_new(name:str, rank:str, unit:str):
    is_create = create_new_soldier(name, rank, unit)
    if not is_create:
        raise HTTPException(status_code=400,detail="adds false")
    return "create"

@app.get("/name-rank",status_code=200)
def give_name_rank():
    return get_names_and_ranks()

@app.get("/ranky",status_code=200)
def get_by_rank(rank: str):
    print("debug in function get by rank")
    answer = get_soldier_by_rank(rank)
    return answer

@app.get("/stats/summary")
def summmary():
    return get_summary()

@app.get("/stats/units")
def units():
    return count_by_unit()

@app.get("/stats/understaffed")
def understaffed():
    my_data = get_units_with_multiple_soldiers()
    return my_data

@app.get("/soldiers/missing-rank")
def missing_rank():
    return get_missing_data()



if __name__ == ("__main__"):
    uvicorn.run("main:app",reload=True)
    