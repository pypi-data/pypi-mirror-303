import requests

class Xbox:
    def __init__(self, api_key):
        self.base_url = "https://xapi.us/v2"
        self.api_key = api_key

    def get_headers(self):
        return {
            'X-Authorization': self.api_key,
            'Content-Type': 'application/json'
        }

    def get_profile(self, gamertag):
        url = f"{self.base_url}/account/{gamertag}"
        headers = self.get_headers()

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve profile: {response.status_code} - {response.text}")
            return None

    def get_achievements(self, xbox_user_id):
        url = f"{self.base_url}/achievements/{xbox_user_id}"
        headers = self.get_headers()

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve achievements: {response.status_code} - {response.text}")
            return None

    def get_game_clips(self, xbox_user_id):
        url = f"{self.base_url}/game-clips/{xbox_user_id}"
        headers = self.get_headers()

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve game clips: {response.status_code} - {response.text}")
            return None
