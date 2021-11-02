import requests
from bs4 import BeautifulSoup
import json
# "https://www.trends.ajio.com/caprese-textured-bi-fold-wallet/p/450134532_orange"


def fetchFromAjio(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}

    response = requests.get(url, headers=headers)

    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    ans1 = soup.find_all('script', {'type': 'application/ld+json'})

    json_obj = json.loads(ans1[2].string)["hasVariant"][0]

    name = json_obj['name']

    price = json_obj['offers']['price']
    return {"name": name, "price": price}
