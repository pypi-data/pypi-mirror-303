import requests

class MyAPIClient:
    def __init__(self,  api_key):
        self.api_key = api_key

    def get_data(self, query, categories="general", engines="all", format="json", count=10):
        endpoint = f"https://shopnobash.com/api/playground-json"
        params = {
            'query': query,
            'api_key': self.api_key,
            'categories': categories,
            'engines': engines,
            'format': format,
            'count': count,
        }
        headers = {'accept': 'application/json'}
        
        response = requests.get(endpoint, params=params, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


