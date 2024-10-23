import requests

class Valorant:
    def __init__(self, api_key, region="na"):
        self.api_key = api_key
        self.region = region 
        self.base_url = f"https://{region}.api.riotgames.com/val"

    def get_account_details(self, puuid):

        url = f"{self.base_url}/content/v1/players/{puuid}"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def get_match_history(self, puuid, count=5):

        url = f"{self.base_url}/match/v1/matchlists/by-puuid/{puuid}?start=0&end={count}"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def get_match_details(self, match_id):

        url = f"{self.base_url}/match/v1/matches/{match_id}"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def get_ranked_info(self, puuid):
        url = f"{self.base_url}/ranked/v1/players/by-puuid/{puuid}"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def get_content(self):
        url = f"{self.base_url}/content/v1/contents"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro {response.status_code}: {response.text}")
            return None