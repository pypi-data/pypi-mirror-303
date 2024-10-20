import requests 
import base64

class VirusTotal:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/api/v3/"
        self.headers = {'x-apikey': self.api_key}

    def get_file_report(self, file_hash):
        url = f"{self.base_url}/files/{file_hash}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)
    
    def scan_url(self, url_to_scan):
        url = f"{self.base_url}/urls"
        data = {'url': url_to_scan}
        response = requests.post(url, headers=self.headers, data=data)
        return self._handle_response(response)
    
    def get_url_report(self, url_to_check):
        url_id = base64.urlsafe_b64encode(url_to_check.encode()).decode().strip("=")
        url = f"{self.base_url}/urls/{url_id}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def scan_file(self, file_path):
        url = f"{self.base_url}/files"
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, headers=self.headers, files=files)
        return self._handle_response(response)

    def get_domain_report(self, domain):
        url = f"{self.base_url}/domains/{domain}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_ip_report(self, ip_address):
        url = f"{self.base_url}/ip_addresses/{ip_address}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_domain_resolutions(self, domain):
        url = f"{self.base_url}/domains/{domain}/resolutions"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_ip_resolutions(self, ip_address):
        url = f"{self.base_url}/ip_addresses/{ip_address}/resolutions"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_comments(self, resource_id):
        url = f"{self.base_url}/comments/{resource_id}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def add_comment(self, resource_id, comment):
        url = f"{self.base_url}/comments"
        data = {
            'data': {
                'type': 'comment',
                'attributes': {
                    'text': comment
                }
            },
            'relationship': {
                'resource': {
                    'data': {
                        'id': resource_id,
                        'type': 'resource'
                    }
                }
            }
        }
        response = requests.post(url, headers=self.headers, json=data)
        return self._handle_response(response)

    def get_multiple_file_reports(self, hashes):
        hash_string = ",".join(hashes)
        url = f"{self.base_url}/files?ids={hash_string}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro {response.status_code}: {response.text}")
            return None