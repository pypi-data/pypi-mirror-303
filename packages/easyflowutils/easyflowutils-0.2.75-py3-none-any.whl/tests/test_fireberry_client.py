import os
from unittest import TestCase, skip

from dotenv import load_dotenv

from easyflowutils import FireberryClient

load_dotenv()


class TestFireberryClient(TestCase):
    token = os.getenv("FIREBERRY_TOKEN")

    def setUp(self):
        self.client = FireberryClient(token=self.token)

    def test_metadata(self):
        metadata = self.client.get_metadata_field_values_dict("33", "statuscode")
        self.assertTrue(metadata)

    def test_get_record(self):
        record = self.client.get_record("AccountProduct", "dfbb8275-d293-4808-95f7-5902252a880f")
        self.assertTrue(record)

    @skip
    def test_create_record(self):
        data = {"accountname": "Nadav",
                "emailaddress1": "nadavtest1@gmail.com",
                "telephone1": "0528393372"}

        record = self.client.create_account(data)
        res = 1

    def test_get_account_by_phone(self):
        account = self.client.get_account_id_by_phone("0528393372")
        self.assertTrue(account)

    def test_get_account_by_email(self):
        account = self.client.get_account_id_by_email("nadavfredi@gmail.com")
        self.assertTrue(account)

    @skip
    def test_create_new_account(self):
        data = {'accountname': ' נדב1', 'emailaddress1': 'nadavnotexistsaccount1@gmail.com', 'telephone1': '0528393371'}
        # res = self.client.create_record("account", data)
        account_res = self.client.create_account(data)
        value = 1

    def test_query(self):
        account_id = "80b58ee6-5a6c-4b5a-b1fe-e2d486ce5fae"
        # account_id = "80b58ee6-5a6c-4b5a-b1fe-e2d486ce5fa9"
        query = f"(accountid = '{account_id}')"

        res = self.client.query(33, query, fields="accountproductid,productid,status")
        self.assertTrue(res)

    def test_get_record_with_int_object_type(self):
        record = self.client.get_record(1, "80b58ee6-5a6c-4b5a-b1fe-e2d486ce5fae")
        self.assertTrue(record)

    @skip
    def test_create_record_with_int_object_type(self):
        data = {
            "accountid": "80b58ee6-5a6c-4b5a-b1fe-e2d486ce5fae",
            "productid": "f7b3f6c5-3a0f-eb11-b1ac-000d3a3e0e6f",
            "statuscode": 1,
            "pcfAccountId": "80b58ee6-5a6c-4b5a-b1fe-e2d486ce5fae"
        }
        record = self.client.create_record(1, data)
        self.assertTrue(record)

    @skip
    def test_create_record_with_str_object_type(self):
        data = {
            "accountid": "80b58ee6-5a6c-4b5a-b1fe-e2d486ce5fae",
            "productid": "f7b3f6c5-3a0f-eb11-b1ac-000d3a3e0e6f",
            "statuscode": 1,
            "pcfAccountId": "80b58ee6-5a6c-4b5a-b1fe-e2d486ce5fae"
        }
        record = self.client.create_record("accountproduct", data)
        self.assertTrue(record)

    def test_add_note_to_object(self):
        note = "test note"
        object_id = "8aac277e-b092-4ae0-85a5-9c72d4cd4139"
        object_type_code = 33
        res = self.client.add_note_to_object(object_type_code, object_id, note)
        self.assertTrue(res)

    def test_get_name_by_id(self):
        object_type = 14
        record_id = "d458c375-9198-4b17-843c-054e3f285208"
        name = self.client.get_name_by_id(object_type, record_id)
        self.assertTrue(name)

    def test_get_query_field_is_one_of(self):
        field_name = "statuscode"
        values = ["1", "2"]
        query = self.client.get_query_field_is_one_of(field_name, values)
        expected_query = "(statuscode = 1) OR (statuscode = 2)"
        self.assertEqual(query, expected_query)
