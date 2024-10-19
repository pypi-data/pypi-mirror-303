from __future__ import annotations
from typing import Any, Optional
import requests
from pydantic import BaseModel


class SchoolerClient:
    BASE_URL = "https://api.schooler.biz"

    def __init__(self, client_id: str, client_secret: str, user_id: str, user_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_id = user_id
        self.user_secret = user_secret
        self.access_token = None
        self.headers = {"Content-Type": "application/json"}

    def authenticate(self) -> SchoolerClient:
        url = f"{self.BASE_URL}/oauth/token"
        data = {
            "grant_type": "password",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "user_id": self.user_id,
            "user_secret": self.user_secret
        }
        response = requests.post(url, json=data)
        response.raise_for_status()
        auth_data = response.json()
        self.access_token = auth_data["access_token"]
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        return self

    def get(self, endpoint: str, params: Optional[dict] = None) -> dict | list[dict]:
        url = f"{self.BASE_URL}/api/v1/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params or {})
        response.raise_for_status()
        return response.json().get("data", {})

    def post(self, endpoint: str, data: dict) -> dict:
        url = f"{self.BASE_URL}/api/v1/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict) -> dict:
        url = f"{self.BASE_URL}/api/v1/{endpoint}"
        response = requests.put(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    # Courses
    def get_courses(self) -> dict:
        return self.get("courses")

    def get_course_details(self, course_id: int) -> dict:
        return self.get(f"courses/{course_id}")

    def get_course_lessons(self, course_id: int) -> dict:
        return self.get(f"courses/{course_id}/lessons")

    def get_course_students(self, course_id: int) -> dict:
        return self.get(f"courses/{course_id}/students")

    def enroll_students_in_course(self, course_id: int, students_data: list[dict]) -> dict:
        return self.post(f"courses/{course_id}/enroll_students", {"students_data": students_data})

    def enroll_single_student_in_course(self, course_id: int, student_data: dict) -> dict:
        return self.post(f"courses/{course_id}/enroll_students", {"students_data": [student_data]})

    def update_students_in_course(self, course_id: int, students_data: list[dict]) -> dict:
        return self.put(f"courses/{course_id}/update_students", {"students_data": students_data})

    def update_single_student_in_course(self, course_id: int, student_data: dict) -> dict:
        return self.put(f"courses/{course_id}/update_students", {"students_data": [student_data]})

    def delete_students_from_course(self, course_id: int, student_ids: list[int]) -> dict:
        return self.post(f"courses/{course_id}/delete_students", {"student_ids": student_ids})

    def delete_single_student_from_course(self, course_id: int, student_id: int) -> dict:
        return self.post(f"courses/{course_id}/delete_students", {"student_ids": [student_id]})

    # Schools
    def get_schools(self) -> dict:
        return self.get("schools")

    def get_school_details(self, school_id: int) -> dict:
        return self.get(f"schools/{school_id}")

    def get_school_students(self, school_id: int) -> dict:
        return self.get(f"schools/{school_id}/students")

    def enroll_students_in_school(self, school_id: int, students_data: list[dict]) -> dict:
        return self.post(f"schools/{school_id}/enroll_students", {"students_data": students_data})

    def update_students_in_school(self, school_id: int, students_data: list[dict]) -> dict:
        return self.put(f"schools/{school_id}/update_students", {"students_data": students_data})

    # Students
    def search_students(self, email: Optional[str] = None, student_id: Optional[int] = None,
                        phone: Optional[str] = None) -> list[dict]:
        params = {}
        if email:
            params["email"] = email
        if student_id:
            params["id"] = student_id
        if phone:
            params["phone"] = phone
        return self.get("students/search", params=params)

    def get_courses_of_student_by_email(self, email: str) -> list[dict]:
        students = self.search_students(email=email)
        single_student = students[0] if students else {}
        return single_student.get("courses", [])
