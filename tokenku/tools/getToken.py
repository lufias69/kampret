import requests
import json

class ApiManager:
    def __init__(self, api_url, username, password):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.headers = {"Content-Type": "application/json"}

    def get_token(self):
        data = {
            "act": "GetToken",
            "username": self.username,
            "password": self.password
        }
        response = requests.post(self.api_url, data=json.dumps(data), headers=self.headers)
        return response.json()


if __name__ == "__main__":
    # Gunakan kelas ApiManager untuk mendapatkan token
    api_url = "http://103.52.114.158/ws/sandbox2.php"
    username = "andikamayansara@gmail.com"
    password = "QkB1LxPlIv"

    api_manager = ApiManager(api_url=api_url, username=username, password=password)
    token_response = api_manager.get_token()

    print(token_response)