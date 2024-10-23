import requests

class TikTok:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://open.tiktokapis.com/v1"
        
    def get_user_profile(self, user_id):
        url = f"{self.base_url}/user/profile/{user_id}"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_user_videos(self, user_id, count=10):
        url = f"{self.base_url}/video/user/{user_id}"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        params = {'count': count}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def search_videos(self, query, count=10):
        url = f"{self.base_url}/video/search"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        params = {'query': query, 'count': count}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def get_trending_videos(self, count=10):
        url = f"{self.base_url}/video/trending"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        params = {'count': count}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def post_video(self, video_data):
        url = f"{self.base_url}/video/create"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.post(url, headers=headers, json=video_data)
        return response.json()
    
    def change_username(self, new_username):
        url = f"{self.base_url}/user/update"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "username": new_username
        }
        
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            print("Username successfully updated to:", new_username)
            return response.json()
        else:
            print("Failed to update username. Status Code:", response.status_code)
            print("Response:", response.json())
            return None

    def delete_video(self, video_id):
        url = f"{self.base_url}/video/{video_id}/delete"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.delete(url, headers=headers)
        return response.status_code == 204

    def get_video_details(self, video_id):
        url = f"{self.base_url}/video/{video_id}"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url, headers=headers)
        return response.json()
