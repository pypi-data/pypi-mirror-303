import requests
import json

class Twitter:
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token
        self.base_url = "https://api.twitter.com/2"

    def create_headers(self):
        return {"Authorization": f"Bearer {self.bearer_token}"}

    def get_user_info(self, username):
        url = f"{self.base_url}/users/by/username/{username}"
        headers = self.create_headers()
        response = requests.get(url, headers=headers)
        return response.json()

    def tweet(self, text):
        url = f"{self.base_url}/tweets"
        headers = self.create_headers()
        data = {"text": text}
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def get_tweets(self, user_id, max_results=5):
        url = f"{self.base_url}/users/{user_id}/tweets"
        headers = self.create_headers()
        params = {"max_results": max_results}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def delete_tweet(self, tweet_id):
        url = f"{self.base_url}/tweets/{tweet_id}"
        headers = self.create_headers()
        response = requests.delete(url, headers=headers)
        return response.status_code == 204
         