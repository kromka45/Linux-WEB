from bs4 import BeautifulSoup
import requests
import json


url = "https://www.battlemetrics.com/servers/reforger/35747535 "
response = requests.get(url)


data_list =[]



soup = BeautifulSoup(response.text, "html.parser")


z= soup.find_all(id="storeBootstrap")




for link in z:
    try:
        data =json.loads(link.text.strip())
        data_list.append(data)
    except json.decoder.JSONDecodeError:
        print("JSON Decode Error")

with open("wynik.json","w",encoding="utf-8") as f:
    json.dump(data_list,f,indent=4,ensure_ascii=False)



