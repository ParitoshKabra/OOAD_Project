import requests
from bs4 import BeautifulSoup
import json

def fetchFromAjio(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'} 

    response= requests.get(url, headers= headers)

    content = response.content
    soup = BeautifulSoup(content,"html.parser")

    ans1= soup.find_all('script', {'type': 'application/ld+json'})

    data= json.loads(ans1[1].string)

    name= data["name"]
    image= data["image"]
    price= data["offers"]["price"]

    print(name, image, price)
    return {"title": name, "price": price, "apiLink": url, "image":image}

