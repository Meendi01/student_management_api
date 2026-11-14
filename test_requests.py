import requests

BASE_URL = "http://127.0.0.1:8000"

student = {
    "name": "John Luke",
    "email": "johnluke@example.com",
    "programme": "Software Engineering",
    "level": 500,
}

created = requests.post(f"{BASE_URL}/students", json=student)
print("POST /students:", created.status_code, created.json())
student_id = created.json()["id"]

listed = requests.get(f"{BASE_URL}/students")
print("GET /students:", listed.status_code, listed.json())

fetched = requests.get(f"{BASE_URL}/students/{student_id}")
print("GET /students/{id}:", fetched.status_code, fetched.json())

updated_student = {
    "name": "John Luke Updated",
    "email": "johnluke@example.com",
    "programme": "Software Engineering",
    "level": 500,
}
updated = requests.put(
    f"{BASE_URL}/students/{student_id}",
    json=updated_student,
)
print("PUT /students/{id}:", updated.status_code, updated.json())

invalid = requests.post(
    f"{BASE_URL}/students",
    json={"name": "Incomplete Student"},
)
print("POST invalid student:", invalid.status_code, invalid.json())

deleted = requests.delete(f"{BASE_URL}/students/{student_id}")
print("DELETE /students/{id}:", deleted.status_code, deleted.json())

missing = requests.get(f"{BASE_URL}/students/{student_id}")
print("GET deleted student:", missing.status_code, missing.json())