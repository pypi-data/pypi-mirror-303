import json
import urllib.request
from typing import Any, Dict

API_URL = 'https://api.rocketscraper.com'

class RocketClient:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError('You must provide a valid API key')
        self.api_key = api_key

    def scrape(self, url: str, schema: Dict[str, Any]) -> Dict[str, Any]:
        if not url:
            raise ValueError('You must provide a valid URL to scrape')
        if not schema:
            raise ValueError('You must provide a valid schema to scrape')

        data = json.dumps({'url': url, 'schema': schema}).encode('utf-8')
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': self.api_key,
        }
        req = urllib.request.Request(f'{API_URL}/scrape', data=data, headers=headers, method='POST')

        try:
            with urllib.request.urlopen(req) as response:
                response_body = response.read()
                if response.status == 200:
                    return json.loads(response_body)
                else:
                    raise Exception(f'HTTP status code {response.status}: {response_body.decode("utf-8")}')
        except urllib.error.URLError as e:
            raise Exception(f'Request error: {str(e)}')