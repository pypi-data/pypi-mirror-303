import requests

class Roblox:
    def __init__(self):
        self.base_url = "https://api.roblox.com"

    def get_user_info(self, username):
        url = f"{self.base_url}/users/get-by-username?username={username}"
        try:
            response = requests.get(url)
            response.raise_for_status()  
            return response.json()
        except requests.ConnectionError:
            print("Failed to connect to the Roblox API. Please check your internet connection.")
            return None
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

    def get_user(self, username):
        user_info = self.get_user_info(username)
        print("User Info:", user_info)
        return user_info

    def get_user_info_by_id(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url)
        return response.json()

    def get_friends(self, user_id):
        url = f"{self.base_url}/users/{user_id}/friends"
        response = requests.get(url)
        return response.json()

    def get_user_games(self, user_id):
        url = f"{self.base_url}/users/{user_id}/games"
        response = requests.get(url)
        return response.json()

    def get_game_details(self, place_id):
        url = f"{self.base_url}/games/get-place-details?placeId={place_id}"
        response = requests.get(url)
        return response.json()

    def get_user_inventory(self, user_id):
        url = f"{self.base_url}/users/{user_id}/inventory"
        response = requests.get(url)
        return response.json()

    def join_game(self, place_id):
        return f"https://www.roblox.com/games/{place_id}"