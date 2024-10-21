import os
from unittest import TestCase

from dotenv import load_dotenv

from easyflowutils.schooler_client import SchoolerClient

load_dotenv()


class TestSchoolerClient(TestCase):
    client_id = os.getenv("SCHOOLER_CLIENT_ID")
    client_secret = os.getenv("SCHOOLER_CLIENT_SECRET")
    user_id = os.getenv("SCHOOLER_USER_ID")
    user_secret = os.getenv("SCHOOLER_USER_SECRET")

    def setUp(self):
        self.client = SchoolerClient(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_id=self.user_id,
            user_secret=self.user_secret
        ).authenticate()

    def test_get_courses(self):
        courses = self.client.get_courses()
        self.assertTrue(courses)
        self.assertIn('data', courses)

    def test_get_course_details(self):
        courses = self.client.get_courses()
        first_course_id = courses['data'][0]['id']

        course_details = self.client.get_course_details(first_course_id)
        self.assertTrue(course_details)
        self.assertIn('data', course_details)

    def test_get_course_lessons(self):
        courses = self.client.get_courses()
        first_course_id = courses['data'][0]['id']

        course_lessons = self.client.get_course_lessons(first_course_id)
        self.assertTrue(course_lessons)
        self.assertIn('data', course_lessons)

    def test_get_course_students(self):
        courses = self.client.get_courses()
        first_course_id = courses['data'][0]['id']

        course_students = self.client.get_course_students(first_course_id)
        self.assertTrue(course_students)
        self.assertIn('data', course_students)

    def test_get_schools(self):
        schools = self.client.get_schools()
        self.assertTrue(schools)
        self.assertIn('data', schools)

    def test_get_school_details(self):
        schools = self.client.get_schools()
        first_school_id = schools['data'][0]['id']

        school_details = self.client.get_school_details(first_school_id)
        self.assertTrue(school_details)
        self.assertIn('data', school_details)

    def test_get_school_students(self):
        schools = self.client.get_schools()
        first_school_id = schools['data'][0]['id']

        school_students = self.client.get_school_students(first_school_id)
        self.assertTrue(school_students)
        self.assertIn('data', school_students)

    def test_search_students(self):
        search_result = self.client.search_students(email="example@email.com")
        self.assertTrue(search_result)
        self.assertIn('data', search_result)
