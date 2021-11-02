import requests
from bs4 import BeautifulSoup

# https://www.flipkart.com/hauser-xo-ball-pen/p/itmaacac4197601c?pid=PENFXKCJMFZ2A4VH&lid=LSTPENFXKCJMFZ2A4VHHU1ZHK&marketplace=FLIPKART&q=pen&store=dgv%2Fmqm&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=b3761e15-96c0-49cc-83f2-52b89102bb77.PENFXKCJMFZ2A4VH.SEARCH&ppt=sp&ppn=sp&ssid=o5yf743ma80000001635315547179&qH=03f00e8e9d0d0847

# https://www.flipkart.com/cello-pinpoint-blue-ball-pen/p/itmf6m4kmnbhjhfx?pid=PENF6M4KZ6V6RNFR&lid=LSTPENF6M4KZ6V6RNFRDYEBAF&marketplace=FLIPKART&q=pen&store=dgv%2Fmqm&srno=s_1_7&otracker=search&otracker1=search&fm=SEARCH&iid=b3761e15-96c0-49cc-83f2-52b89102bb77.PENF6M4KZ6V6RNFR.SEARCH&ppt=sp&ppn=sp&ssid=o5yf743ma80000001635315547179&qH=03f00e8e9d0d0847

# https://www.flipkart.com/zara-angel-solid-women-waistcoat/p/itme101de971d58c?pid=WSCG6Z3PH78PGVHF&lid=LSTWSCG6Z3PH78PGVHFPBG1XM&marketplace=FLIPKART&store=clo%2Fupk%2F8mn%2Fely&srno=b_1_1&otracker=hp_reco_Winter%2BEssentials_4_4.dealCard.OMU_cid%3AS_F_N_clo_upk_8mn_ely__d_60-100__NONE_ALL%3Bnid%3Aclo_upk_8mn_ely_%3Bet%3AS%3Beid%3Aclo_upk_8mn_ely_%3Bmp%3AF%3Bct%3Ad%3B_3&otracker1=hp_reco_SECTIONED_manualRanking_personalisedRecommendation%2FC5_Winter%2BEssentials_DESKTOP_HORIZONTAL_dealCard_cc_4_NA_view-all_3&fm=personalisedRecommendation%2FC5&iid=0b63f0bb-2692-4160-9dbf-2945ec634d7f.WSCG6Z3PH78PGVHF.SEARCH&ppt=hp&ppn=homepage&ssid=cobbjedsj40000001635317594082

# https://www.flipkart.com/cello-butterflow-simply-ball-pen-jar/p/itmf8a2esehnqsc2?pid=PENF8A2E7G94HZG4&lid=LSTPENF8A2E7G94HZG4WZRUYI&marketplace=FLIPKART&q=pen&store=dgv%2Fmqm&spotlightTagId=BestsellerId_dgv%2Fmqm&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=b3761e15-96c0-49cc-83f2-52b89102bb77.PENF8A2E7G94HZG4.SEARCH&ppt=sp&ppn=sp&ssid=o5yf743ma80000001635315547179&qH=03f00e8e9d0d0847


def fetchFromFlipkart(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}

    response = requests.get(url, headers=headers)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    # name
    for item in soup.find_all('span'):
        if "pen" in item.text:
            print(item.text)
    ans = soup.find('span', {'class': 'css-901oao'})
    name = ans.text
    print(name)

    # price
    ans1 = soup.find_all('div', {'class': 'css-901oao'})
    price = None
    for a in ans1:
        try:
            if(a.text[0] == '₹'):
                price = a.text
                print(price)
                break
        except:
            print("no")
    return {"name": name, "price": price}

# ans2= soup.find_all('img')
# print(ans2[4].attrs)
