from typing import Any, Optional

import requests

ACCOUNT_OBJECT_CODE = 1
CRM_USERS_OBJECT_CODE = 9


class FireberryClient:
    BASE_URL = "https://api.fireberry.com"
    API_URL = f"{BASE_URL}/api"

    ACCOUNT_ID_KEY = "accountid"

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "tokenid": self.token,
            "Content-Type": "application/json"
        }

    def get(self, endpoint: str, params: Optional[dict[str, Any]] = None, prefix=API_URL) -> dict[str, Any]:
        url = f"{prefix}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params or {})
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict[str, Any], prefix=API_URL) -> dict[str, Any] | list[dict[str, Any]]:
        url = f"{prefix}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.API_URL}/{endpoint}"
        response = requests.put(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> dict[str, Any]:
        url = f"{self.API_URL}/{endpoint}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def query(self, object_type_code: int, query: str, fields: Optional[str] = None) -> list[dict[str, Any]]:
        data = {
            "objecttype": object_type_code,
            "query": query,
        }
        if fields:
            data["fields"] = fields
        return self.post('query', data).get("data", {}).get("Data", [])

    def get_metadata_field_values(self, object_type_code: str | int, field_name: str) -> dict[str, Any]:
        return self.get(f"metadata/records/{object_type_code}/fields/{field_name}/values", prefix=self.BASE_URL)

    def get_metadata_field_names_dict(self, object_type_code: str | int, field_name: str) -> dict[str, Any]:
        field_values = self.get_metadata_field_values(object_type_code, field_name)
        return {item['name']: item for item in field_values.get("data", {}).get("values", {})}

    def get_metadata_field_values_dict(self, object_type_code: str | int, field_name: str) -> dict[str, Any]:
        field_values = self.get_metadata_field_values(object_type_code, field_name)
        return {item['value']: item for item in field_values.get("data", {}).get("values", {})}

    def get_record(self, object_type: str | int, record_id: str) -> dict[str, Any]:
        return self.get(f"record/{object_type}/{record_id}").get("data", {}).get("Record", {})

    def get_multiple_records(self, object_type: str | int, fields: Optional[list[str]] = None) -> list[dict[str, Any]]:
        records = self.get(f"record/{object_type}").get("data", {}).get("Records", [])
        if fields:
            return [{field: record.get(field) for field in fields} for record in records]
        return records

    def get_crm_users(self, fields: Optional[list[str]] = None) -> list[dict[str, Any]]:
        return self.get_multiple_records(CRM_USERS_OBJECT_CODE, fields)

    def get_crm_users_ids(self) -> list[str]:
        return [user.get("crmuserid") for user in self.get_crm_users()]

    def create_record(self, object_type: str | int, data: dict[str, Any]) -> dict[str, Any]:
        return self.post(f"record/{object_type}", data).get("data", {}).get("Record", {})

    def update_record(self, object_type: str | int, record_id: str, data: dict[str, Any]) -> dict[str, Any]:
        return self.put(f"record/{object_type}/{record_id}", data).get("record", {})

    def delete_record(self, object_type: str | int, record_id: str) -> dict[str, Any]:
        return self.delete(f"record/{object_type}/{record_id}")

    def batch_update(self, object_type: str | int, data: list[dict[str, Any]]) -> dict[str, Any]:
        api_prefix = "https://api.fireberry.com/api/v3/record"
        endpoint = f'{object_type}/batch/update'
        payload = {"data": data}
        return self.post(prefix=api_prefix, endpoint=endpoint, data=payload)

    def batch_create(self, object_type: str | int, data: list[dict[str, Any]]) -> dict[str, Any]:
        api_prefix = "https://api.fireberry.com/api/v3/record"
        endpoint = f'{object_type}/batch/create'
        payload = {"data": data}
        return self.post(prefix=api_prefix, endpoint=endpoint, data=payload)

    def batch_delete(self, object_type: str | int, data: list[str]) -> list[dict[str, Any]]:
        api_prefix = "https://api.fireberry.com/api/v3/record"
        endpoint = f'{object_type}/batch/delete'

        results = []
        for i in range(0, len(data), 20):
            payload = {"data": data[i:i + 20]}
            results.append(self.post(prefix=api_prefix, endpoint=endpoint, data=payload))

        return results

    def add_note_to_object(self, object_type_code: int, object_id: str, note_text: str) -> dict[str, Any]:
        body = {
            "objectid": object_id,
            "notetext": note_text,
            "objecttypecode": object_type_code,
        }
        return self.create_record("note", body)

    def create_account(self, data: dict[str, Any]) -> dict[str, Any]:
        return self.create_record("account", data)

    def get_account_by_id(self, account_id: str) -> dict[str, Any]:
        return self.get_record(ACCOUNT_OBJECT_CODE, account_id)

    def get_account_by_field_and_value(self, field_name: str, value: str) -> Optional[dict[str, Any]]:
        query = f"({field_name} = '{value}')"
        data = self.query(ACCOUNT_OBJECT_CODE, query)
        if data:
            return data[0]
        return None

    def get_account_by_email(self, email: str) -> Optional[dict[str, Any]]:
        return self.get_account_by_field_and_value("emailaddress1", email)

    def get_account_by_phone(self, phone: str) -> Optional[dict[str, Any]]:
        return self.get_account_by_field_and_value("telephone1", phone)

    def get_account_id_by_email(self, email: str) -> Optional[str]:
        account = self.get_account_by_email(email)
        if account:
            return account.get(self.ACCOUNT_ID_KEY)
        return None

    def get_account_id_by_phone(self, phone: str) -> Optional[str]:
        account = self.get_account_by_phone(phone)
        if account:
            return account.get(self.ACCOUNT_ID_KEY)
        return None

    def delete_account_by_id(self, account_id: str) -> dict[str, Any]:
        return self.delete_record(ACCOUNT_OBJECT_CODE, account_id)

    def query_all_crm_users(self) -> list[dict]:
        return self.query(ACCOUNT_OBJECT_CODE, "pcfIsUser = 1", "crmuserid")

    @classmethod
    def get_record_url_of_object(cls, object_type_code: int, object_id: str) -> str:
        app_url = "https://app.fireberry.com/app"
        return f"{app_url}/record/{object_type_code}/{object_id}"

    def get_name_by_id(self, object_type: str | int, record_id: str) -> str:
        record = self.get_record(object_type, record_id)
        return record.get("name", "")

    @classmethod
    def get_query_field_is_one_of(cls, field_name: str, values: list[str | int]) -> str:
        query_conditions = []
        for value in values:
            query_conditions.append(f"({field_name} = {value})")

        return " OR ".join(query_conditions)
