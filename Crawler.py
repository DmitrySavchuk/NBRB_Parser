import requests


class Crawler:
    def __init__(self, _url):
        self.url = _url
        self.rates = None

    def get_response(self):
        self.rates = requests.get(self.url)

        return self.rates.text
