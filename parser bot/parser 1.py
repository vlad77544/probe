import requests

from bs4 import BeautifulSoup
import json


# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
# headers = {
#     'Accept': '*/*' ,
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)
#
# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)

with open('index.html', encoding='utf-8') as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml")
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")

all_categories_dict = {}
for item in all_products_hrefs:
    item_text = item.text
    item_herf = "https://health-diet.ru" + item.get("href")
    # print(f"{item_text}: {item_herf}")
    # print(item)

    all_categories_dict[item_text] = item_href

with open("all_categories_dict.json", "w") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
    # lgndrbnd
