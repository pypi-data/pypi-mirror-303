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
        
        try:
            response = requests.get(endpoint, params=params, headers=headers)
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # Customize the error message
            raise Exception("API request failed with status code: {}".format(response.status_code))
        except Exception as err:
            raise Exception("An error occurred: {}".format(str(err)))


