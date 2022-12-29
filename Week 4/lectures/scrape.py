import pandas as pd
import requests 
from bs4 import BeautifulSoup
Product_name = []
Prices = []
url = "https://www.flipkart.com/search?q=mobile+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+under+10000%7CMobiles&requestId=69e3bdd6-37c2-4c0e-becb-9a32a8564dd8&as-searchtext=mobile%20under"


r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "html")

names = soup.find_all("div", class_ = "_4rR01T")

for i in names:
    name = i.text
    Product_name.append(name)
    print(len(Product_name))


Prices = soup.find_all("div", class_ = "_4rR01T")

for i in Prices:
    Prices = i.text
    Product_name.append(Prices)
    print(len(Prices))