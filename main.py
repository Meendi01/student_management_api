from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student Management API", version="1.0.0")

class Student(BaseModel):
    name: str
    email: str
    programme: str
    level: int

students = []

@app.post("/students", status_code=201)
def create_student(student: Student):
    new_student = {"id": len(students) + 1, **student.model_dump()}
    students.append(new_student)
    return new_student

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for index, existing in enumerate(students):
        if existing["id"] == student_id:
            updated = {"id": student_id, **student.model_dump()}
            students[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(index)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")