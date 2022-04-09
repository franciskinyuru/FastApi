#Have python 3.6 or more installed in your computer
#install required packages with below commands
# Pip install fastapi, uvicorn

# import all required packages as below
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()
# we are going to experiment below CRUD operations
# GET- GET object data
# POST- Create new object
# PUT- Update an Object
# Delete - delete object

# To You application use below command 
# uvicorn startapi:app --reload
# visit  http://127.0.0.1:8000 after you run the app then visit  http://127.0.0.1:8000/docs for all the apis created below.



# create a dictionary by the name student and add one student as below
students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}


# class Student will help us add a new student in the POST Method
class Student(BaseModel):
    name: str
    age: int
    year: str

# UpdateStudent will help us Update student details 
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


#first Api will be get method as below
@app.get("/")
def home():
    return {"name": "First Data"}


#get method with params passed 
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0)):
    return students[student_id]


# Get method with query params plus optional params/args feature

@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"Data": "Not found"}


# Get method with combining Path ahd Query parameters

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"Data": "Not found"}


#Post method with Request Body and The post Method we use this to create a new student 
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id] 


# Put method to update student details
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

# delete method to delete Student 

@app.delete("/delete_student/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "Student Does not exist"}
    del students[student_id]
    return {"message": "Student Deleted Successfully"}

See below my apis clear above.
![img.png](img.png)

# Happy coding :)
