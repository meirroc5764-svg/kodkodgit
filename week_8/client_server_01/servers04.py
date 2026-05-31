import uvicorn
from fastapi import FastAPI

app = FastAPI()

grades = {"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92}}


@app.get("/students")
def get_show_all():
    '''returns all students'''
    return grades

@app.get("/students/top")
def get_show_top(): 
    '''returns the student with the highest grade'''
    the_best = max(grades.values(),key=lambda studens:studens["grade"])
    return {"the best student":the_best}

@app.get("/students/average")
def get_show_averge(): 
    '''returns the class average'''
    the_class_greade_sum = sum(studens["grade"] for studens in grades.values())
    return {"the class averge":the_class_greade_sum / len(grades)}

@app.get("/students/count")
def get_show_(): 
    '''returns the number of students'''
    return {"the class count":len(grades)}

@app.get("/students/{student_id}")
def show_one(student_id):
    ''' returns one student'''
    return {f"this information of student {student_id}":grades[student_id]}





if __name__ == "__main__":
    uvicorn.run("servers04:app", host="127.0.0.1", port=8000, reload=True)
