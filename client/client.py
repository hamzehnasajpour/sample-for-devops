import requests
import json

class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    def set_rate(self, currency_pair, rate):
        url = f'{self.base_url}/set_rate1'
        data = {'currency_pair': currency_pair, 'rate': rate}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response.json()

    def get_rate(self, currency_pair):
        url = f'{self.base_url}/get_rate'
        params = {'currency_pair': currency_pair}
        response = requests.get(url, params=params)
        return response.json()
