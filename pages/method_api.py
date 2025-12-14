import requests
from config import USER_AGENT, ORIGIN_URL


class API:
    def __init__(self, base_url):
        self.base_url = base_url

    def search(self, bearer_token: str, phrase: str):
        """
        Поиск по ключевым словам
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer_token}",
            "referer": ORIGIN_URL+"/",
            "Origin": ORIGIN_URL,
            "User-Agent": USER_AGENT
        }

        params = {
            "customerCityId": 213,
            "phrase": phrase,
            "abTestGroup": 1,
            "suggests[page]": 1,
            "suggests[per-page]": 5,
            "include": "authors,bookCycles,categories,publishers,publisherSeries,products"
        }

        req = requests.get(
            self.base_url + "/search-phrase-suggests",
            headers=headers,
            params=params
        )

        return req
