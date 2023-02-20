from decouple import config
import requests


class DataManager:

    SHEET_ENDPOINT = "https://api.sheety.co/ca47c9deea0a4e895b4db204de01f66a/flightDeals/prices"
    HEADER = {
        "Authorization": config("SHEET_API_KEY")
    }
    USER_SHEET_ENDPOINT = "https://api.sheety.co/ca47c9deea0a4e895b4db204de01f66a/flightDeals/users"

    def get_sheet(self):
        response = requests.get(url=self.SHEET_ENDPOINT, headers=self.HEADER)
        return response.json()

    def update_row(self, row_id, row_data):
        put_url = self.SHEET_ENDPOINT + f"/{row_id}"
        response = requests.put(url=put_url, headers=self.HEADER, json=row_data)
        print(response.text)

    def add_user(self, row_data):
        response = requests.post(url=self.USER_SHEET_ENDPOINT, headers=self.HEADER, json=row_data)
        print(response.text)

    def get_users_sheet(self):
        response = requests.get(url=self.USER_SHEET_ENDPOINT, headers=self.HEADER)
        return response.json()
