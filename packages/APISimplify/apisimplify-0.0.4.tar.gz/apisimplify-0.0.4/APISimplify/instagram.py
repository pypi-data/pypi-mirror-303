import requests

class Instagram:
    def __init__(self, access_token):
        self.base_url = 'https://graph.instagram.com'
        self.access_token = access_token

    def get_user_profile(self):
        url = f"{self.base_url}/me"
        params = {
            'fields': 'id,username,account_type,media_count',
            'access_token': self.access_token
        }
        response = requests.get(url, params=params)
        
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
    
    def get_user_info(self):
        user_profile = self.get_user_profile()
        
        if user_profile:
            user_info = {
                'User ID': user_profile.get('id'),
                'Username': user_profile.get('username'),
                'Account Type': user_profile.get('account_type'),  
                'Media Count': user_profile.get('media_count'),
            }
            return user_info
        else:
            return None

    def print_user_info(self):
        user_info = self.get_user_info()
        
        if user_info:
            print("User Information:")
            print(f"User ID: {user_info['User ID']}")
            print(f"Username: {user_info['Username']}")
            print(f"Account Type: {user_info['Account Type']}")
            print(f"Media Count: {user_info['Media Count']}")
        else:
            print("Could not retrieve user information.")
