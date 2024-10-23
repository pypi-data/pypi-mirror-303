import requests
import time

class EasyApi:
    def __init__(self, base_url, access_token=None, default_timeout=10):
        self.base_url = base_url
        self.access_token = access_token
        self.default_timeout = default_timeout  

    def get(self, endpoint, params=None, headers=None, timeout=None):
        url = f"{self.base_url}/{endpoint}"
        headers = self._build_headers(headers)

        response = requests.get(url, headers=headers, params=params, timeout=timeout or self.default_timeout)
        return self.handle_response(response)

    def post(self, endpoint, data=None, headers=None, files=None, timeout=None):
        url = f"{self.base_url}/{endpoint}"
        headers = self._build_headers(headers)

        response = requests.post(url, headers=headers, json=data, files=files, timeout=timeout or self.default_timeout)
        return self.handle_response(response)

    def put(self, endpoint, data=None, headers=None, timeout=None):
        url = f"{self.base_url}/{endpoint}"
        headers = self._build_headers(headers)

        response = requests.put(url, headers=headers, json=data, timeout=timeout or self.default_timeout)
        return self.handle_response(response)

    def delete(self, endpoint, headers=None, timeout=None):
        url = f"{self.base_url}/{endpoint}"
        headers = self._build_headers(headers)

        response = requests.delete(url, headers=headers, timeout=timeout or self.default_timeout)
        return self.handle_response(response)

    def _build_headers(self, custom_headers=None):
        headers = custom_headers if custom_headers else {}
        if self.access_token:
            headers['Authorization'] = f'Bearer {self.access_token}'
        return headers

    def handle_response(self, response):
        if 200 <= response.status_code < 300:
            try:
                return response.json()
            except ValueError:
                print("Error: Response content is not valid JSON.")
                return None
        elif response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 1))
            print(f"Rate limit exceeded, retrying in {retry_after} seconds...")
            time.sleep(retry_after)
            return None
        elif response.status_code == 500:
            print(f"Server error: {response.status_code}")
            return None
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None