SENG 863 LAB PRACTICAL 2: STUDENT MANAGEMENT REST API

Student: [Your name]
Date: 14 November 2026

OBJECTIVE
Build, document, and test a Student Management REST API using Python and FastAPI.

PROJECT SETUP
Project folder: student_management_api
Python: 3.15.2
FastAPI: 0.162.7
Uvicorn: 0.54.0
Requests: 2.34.2
Dependencies are recorded in requirements.txt. Git was initialized and used to track the project.

STUDENT DATA MODEL
Each student record contains:
- ID, assigned by the API
- Name
- Email
- Programme
- Level

API ENDPOINTS
POST /students — Create a student. Successful response: 201 Created.
GET /students — Return the student list.
GET /students/{student_id} — Return one student, or 404 if not found.
PUT /students/{student_id} — Replace a student's details, or 404 if not found.
DELETE /students/{student_id} — Delete a student, or 404 if not found.

TEST RESULTS

Swagger/OpenAPI:
- POST /students — 201 Created; student record returned. PASS
- GET /students — 200 OK; created student listed. PASS
- GET /students/1 — 200 OK; John Luke's record returned. PASS
- PUT /students/1 — 200 OK; updated record returned. PASS
- DELETE /students/1 — 200 OK; deletion message returned. PASS
- GET /students/1 after deletion — 404 Not Found. PASS

Postman:
- GET /students/1 after deletion — response body: {"detail":"Student not found"}.
- Record the status shown in Postman: 404 Not Found.

Python Requests:
- POST /students — 201 Created. PASS
- GET /students — 200 OK. PASS
- GET /students/{id} — 200 OK. PASS
- PUT /students/{id} — 200 OK. PASS
- POST with missing required fields — 422 Unprocessable Entity. PASS
- DELETE /students/{id} — 200 OK. PASS
- GET the deleted student — 404 Not Found. PASS

CONCLUSION
The API supports the required create, read, update, and delete operations. 
Pydantic validation rejects incomplete student data, and the API returns 404 when a requested student does not exist. 
Swagger/OpenAPI, Postman, and Python Requests were used to exercise the API.