import requests

class DiscordAuth:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = "https://discord.com/api/oauth2/token"
        self.scope = 'bot'

    def get_token(self):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials',
            'scope': self.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(self.token_url, data=data, headers=headers)

        if response.status_code == 200:
            token_info = response.json()
            access_token = token_info['access_token']
            return access_token
        else:
            raise Exception(f"Failed to obtain token. Status code: {response.status_code}, Response: {response.text}")