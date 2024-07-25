import requests
import jwt 
from datetime import datetime as date
from django.conf import settings

class GhostService:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def _generate_token(self):
        # Split the key into ID and SECRET
        id, secret = self.api_key.split(':')
         # Prepare header and payload
        iat = int(date.now().timestamp())

        header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
        payload = {
            'iat': iat,
            'exp': iat + 5 * 60,
            'aud': '/admin/'
        }

        # Create the token (including decoding secret)
        token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)
        print(token)
        return token

    def create_post(self, title, content):
        token = self._generate_token()
        url = f"{self.api_url}/posts/?source=html"
        headers = {'Authorization': f'Ghost {token}'}
        data = {
            "posts": [{
                "title": title,
                "html": f"<p>{content}</p>",
                "status": "published"
            }]
        }
        response = requests.post(url, json=data, headers=headers)
        print(response.text)
        print(title)
        print(content)
        return response.json()
