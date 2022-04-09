from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# GET- GET object data
# POST- Create new object
# PUT- Update an Object
# Delete - delete object

# run app
##  uvicorn startapi:app --reload

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def home():
    return {"name": "First Data"}


# pass params
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0)):
    return students[student_id]


# query params

@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"Data": "Not found"}


# combining Path ahd Query parameters

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"Data": "Not found"}


# Request Body and The post Method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]


# Put method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    if student.name is not None:
        students[student_id].name = student.name
    if student.age is not None:
        students[student_id].age = student.age
    if student.year is not None:
        students[student_id].year = student.year
    return students[student_id]

# delete method

@app.delete("/delete_student/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "Student Does not exist"}
    del students[student_id]
    return {"message": "Student Deleted Successfully"}
