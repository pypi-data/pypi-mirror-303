#unofficial api

import requests

class LibreView:
    def __init__(self, email, password):
        self.base_url = "https://api.libreview.io"
        self.email = email
        self.password = password
        self.token = None

    def login(self):
        url = f"{self.base_url}/uaa/oauth/token"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'password',
            'username': self.email,
            'password': self.password,
            'client_id': 'diabetes-client-id' 
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            self.token = response.json().get("access_token")
            print(f"Logged in successfully. Access Token: {self.token}")
        else:
            print(f"Login failed: {response.status_code} - {response.text}")

    def get_glucose_data(self):
        if not self.token:
            print("You must log in first.")
            return
        
        url = f"{self.base_url}/data/sensor/glucose"
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve glucose data: {response.status_code} - {response.text}")
            return None