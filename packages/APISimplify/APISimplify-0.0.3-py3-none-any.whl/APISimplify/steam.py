import requests

class Steam:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.steampowered.com"

    def get_user_summary(self, steam_id):
        url = f"{self.base_url}/ISteamUser/GetPlayerSummaries/v0002/"
        params = {
            'key': self.api_key,
            'steamids': steam_id
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'response' in data and 'players' in data['response']:
                return data['response']['players'][0]
        return None

    def get_owned_games(self, steam_id):
        url = f"{self.base_url}/IPlayerService/GetOwnedGames/v0001/"
        params = {
            'key': self.api_key,
            'steamid': steam_id,
            'include_appinfo': True,
            'include_played_free_games': True
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'response' in data and 'games' in data['response']:
                return data['response']['games']
        return None

    def get_friend_list(self, steam_id):
        url = f"{self.base_url}/ISteamUser/GetFriendList/v0001/"
        params = {
            'key': self.api_key,
            'steamid': steam_id,
            'relationship': 'friend'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'friendslist' in data and 'friends' in data['friendslist']:
                return data['friendslist']['friends']
        return None

    def get_player_achievements(self, steam_id, app_id):
        url = f"{self.base_url}/ISteamUserStats/GetPlayerAchievements/v0001/"
        params = {
            'key': self.api_key,
            'steamid': steam_id,
            'appid': app_id
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'playerstats' in data and 'achievements' in data['playerstats']:
                return data['playerstats']['achievements']
        return None

    def get_game_details(self, app_id):
        url = f"http://store.steampowered.com/api/appdetails/"
        params = {
            'appids': app_id
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if str(app_id) in data and data[str(app_id)]['success']:
                return data[str(app_id)]['data']
        return None