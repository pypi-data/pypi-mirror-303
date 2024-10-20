import requests

class BloxFlip:
    def __init__(self, session_token):
        self.base_url = 'https://api.bloxflip.com/v1'
        self.session_token = session_token

    def get_user_balance(self):
        url = f"{self.base_url}/user/balance"
        headers = {
            'Authorization': f'Bearer {self.session_token}'
        }
        response = requests.get(url, headers=headers)

        print(f"Request URL: {response.url}")  
        print(f"Response Status Code: {response.status_code}")  

        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                print("Error: Response content is not valid JSON.")
                return None
        else:
            print(f"Error: {response.status_code} - {response.text}")  
            return None

    def get_recent_bets(self):
        url = f"{self.base_url}/user/bets"
        headers = {
            'Authorization': f'Bearer {self.session_token}'
        }
        response = requests.get(url, headers=headers)
        
        print(f"Request URL: {response.url}")  
        print(f"Response Status Code: {response.status_code}")  

        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                print("Error: Response content is not valid JSON.")
                return None
        else:
            print(f"Error: {response.status_code} - {response.text}")  
            return None

    def print_user_info(self):
        balance_info = self.get_user_balance()
        bets_info = self.get_recent_bets()

        if balance_info and bets_info:
            print("User Information:")
            print(f"Balance: {balance_info.get('balance', 0)}")
            print("Recent Bets:")
            for bet in bets_info.get('bets', []):
                print(f" - Amount: {bet.get('amount')}, Result: {bet.get('result')}")
        else:
            print("Could not retrieve user information.")