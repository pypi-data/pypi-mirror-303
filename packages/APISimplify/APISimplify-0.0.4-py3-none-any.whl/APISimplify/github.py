import requests

class GitHub:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://api.github.com"

    def get_user_info(self):
        url = f"{self.base_url}/user"
        headers = {'Authorization': f'token {self.access_token}'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            user_info = response.json()
            
            print("User Information:")
            print(f"Username: {user_info.get('login')}")
            print(f"User ID: {user_info.get('id')}")
            print(f"Profile URL: {user_info.get('html_url')}")
            print(f"Public Repositories: {user_info.get('public_repos')}")
            print(f"Followers: {user_info.get('followers')}")
            print(f"Following: {user_info.get('following')}")
            print(f"Bio: {user_info.get('bio')}")
            print(f"Location: {user_info.get('location')}")
            
            return user_info
        else:
            print(f"Error: {response.status_code} - {response.json().get('message')}")
            return None

    def list_repositories(self):
        url = f"{self.base_url}/user/repos"
        headers = {'Authorization': f'token {self.access_token}'}
        response = requests.get(url, headers=headers)
        return response.json()

    def create_repository(self, repo_name, private=True, description="", readme=True, gitignore=None, license_template=None):
        url = f"{self.base_url}/user/repos"
        headers = {
            'Authorization': f'token {self.access_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {
            'name': repo_name,
            'private': private,
            'description': description,
            'has_issues': True,
            'has_projects': True,
            'has_wiki': True,
            'auto_init': readme
        }

        response = requests.post(url, headers=headers, json=data)
        repo_info = response.json()

        if response.status_code == 201:
            print(f"Repository '{repo_name}' created successfully.")

            if readme:
                self.create_file(repo_name, 'README.md', '# ' + repo_name + '\n' + description)

            if gitignore:
                self.create_file(repo_name, '.gitignore', gitignore)

            if license_template:
                self.create_file(repo_name, 'LICENSE', license_template)

            return repo_info
        else:
            print(f"Error: {response.status_code} - {repo_info.get('message')}")
            return None
        
    def get_available_licenses(self):
        url = "https://api.github.com/licenses"
        response = requests.get(url)
        if response.status_code == 200:
            licenses = response.json()
            return {license['spdx_id']: license['name'] for license in licenses}
        else:
            print(f"Error fetching licenses: {response.status_code} - {response.json().get('message')}")
            return None

    def get_gitignore_templates(self):
        return {
            'Python': "*.pyc\n__pycache__/\n",
            'Node': "node_modules/\n",
            'Java': "*.class\n*.jar\n",
            'Ruby': "*.gem\n*.rbc\n",
            'C++': "*.o\n*.out\n",
            'JavaScript': "node_modules/\n",
            'Visual Studio': "bin/\nobj/\n",
            'MacOS': ".DS_Store\n",
            'Windows': "Thumbs.db\n"
        }

    def delete_repository(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}"
        headers = {'Authorization': f'token {self.access_token}'}
        response = requests.delete(url, headers=headers)
        return response.status_code == 204

    def create_issue(self, owner, repo, title, body=""):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        headers = {
            'Authorization': f'token {self.access_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {
            'title': title,
            'body': body
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def list_issues(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        headers = {'Authorization': f'token {self.access_token}'}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_repository(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}"
        headers = {'Authorization': f'token {self.access_token}'}
        response = requests.get(url, headers=headers)
        return response.json()
    
    def get_username(self):
        user_info = self.get_user_info()
        current_username = user_info.get('login')

    def create_file(self, repo_name, file_path, content):
        url = f"{self.base_url}/repos/{self.get_user()}/{repo_name}/contents/{file_path}"
        headers = {
            'Authorization': f'token {self.access_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {
            'message': f'Create {file_path}',
            'content': self.encode_content(content)
        }
        response = requests.put(url, headers=headers, json=data)
        return response.json()
    
    def change_display_name(self, new_name):
        url = f"{self.base_url}/user"
        headers = {
            'Authorization': f'token {self.access_token}',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
        }
        data = {
            "name": new_name 
        }

        response = requests.patch(url, headers=headers, json=data)
        
        if response.status_code == 200:
            print("Display name successfully updated to:", new_name)
            return response.json()
        else:
            print("Failed to update display name. Status Code:", response.status_code)
            print("Response:", response.json())
            return None

    def change_name(self, new_name):
        url = f"{self.base_url}/user"
        headers = {
            'Authorization': f'token {self.access_token}',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
        }
        data = {
            'name': new_name
        }
        
        response = requests.patch(url, headers=headers, json=data)
        
        if response.status_code == 200:
            print("Name successfully updated to:", new_name)
            return response.json()
        else:
            print("Failed to update name. Status Code:", response.status_code)
            print("Response:", response.json())
            return None
