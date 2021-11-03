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

    ans1= soup.find_all('script')
    res= ans1[12].string[34:-4]
    index1= res.index("images")
    index2= res.index("\"isShopTheLookAvailable\"")
    res1=res[index1:index2]
    index3= res1.index("images")
    index4= res1.index("isReturnable")
    data= json.loads(res1[index3+8:index4-2])

    # image
    image= data[0]["url"]

    return {"title": name, "price": price, "apiLink": url, "image":image}




    
    
