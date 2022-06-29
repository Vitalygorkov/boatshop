import sqlite3
import requests
import json
import time
from random import randint
from bs4 import BeautifulSoup

conn = sqlite3.connect('price.db')
cur = conn.cursor()
# создаем таблицу
cur.execute("""CREATE TABLE IF NOT EXISTS price(
   product_id INT PRIMARY KEY,
   product_name TEXT,
   parse_url TEXT,
   price_change TEXT,
   price INT);
""")
conn.commit()

# {'id': 4, 'name': 'Ривьера Компакт 3600 СК "Комби" светло-серый/черный', 'image': 'http://localhost:8000/media/photo/71_QhvXdTw.png', 'manufacturer': {'id': 2, 'name': 'Мастер лодок', 'description': 'г. Уфа'}, 'price': 59560, 'product_abs_url': '/slan-keel/lodka-rivera-3600-kilevoe-naduvnoe-dno-kombi-svetlo-seryjchernyj', 'sale': 0, 'color': {'id': 1, 'name': 'Светло-серый/Чёрный'}, 'category': 13, 'slug': 'lodka-rivera-3600-kilevoe-naduvnoe-dno-kombi-svetlo-seryjchernyj', 'parse_url': 'https://master-lodok.ru/catalog/lodki/rivera/rivera_kompakt/rivera_kompakt_3600_sk_kombi_svetlo_seryy_chernyy_/'}


# headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
#                          "KHTML, like Gecko) Version/4.0 Safari/534.30"}

headers = {"User-Agent": "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/31.0.1650.0 Safari/537.36"}

        # берем сет товаров
url_api = 'https://vitgo.ru/api/v1/products/'
rs = requests.get(url_api)
        # берем сет товаров
    # (url_api, params=params, headers=headers)
count = 0

# for only master- lodok
for item in rs.json():
    if count > 100:
        count += 1
        print(count)
        break
    print(item)
    delay = randint(1, 4)
    time.sleep(delay)
    if item.get('parse_url') != None:
        url = item.get('parse_url')
        print(item.get('id'))
        print(item.get('parse_url'))
        response = requests.get(url, headers=headers, verify=False)
        webpage = response.content
        soup = BeautifulSoup(webpage, "html.parser")
        price = soup.find_all("div", class_="item_current_price")
        print(price)
        print('старая цена', item.get('price'))
        new_price = price[0].attrs["data-price"]
        print('новая цена', new_price)
        if item.get('price') != price[0].attrs["data-price"]:
            print('цена изменилась')
            api_product_url = url_api + str(item.get('id'))+'/'
            print(api_product_url)
            print('цена изменилась')
            item['price'] = new_price
            print(item)
            new_name = item.get('name')
            print(new_name)
            new_slug = item.get('slug')
            print(new_slug)
            new_item = {
                "id": item.get('id'),
                "name": new_name.encode('utf-8'),
                "price": new_price,
                "slug": new_slug.encode('utf-8'),
            }
            response2 = requests.put(api_product_url, data=new_item)
            print(response2.status_code)
            print(response2.content)
            # request.put(api_\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f\xd1\x85product_url, paraitem_idms={key: value})
    count +=1







        # -- Парсинг --
# url = 'https://master-lodok.ru/catalog/lodki/rivera/rivera_ndnd_gidrolyzha/rivera_3200_ndnd_gidrolyzha_kombi_svetlo_seryy_grafit_/'
# response = requests.get(url, headers=headers, verify = False)
# webpage = response.content
# soup = BeautifulSoup(webpage, "html.parser")
#
#
# for price in soup.find_all("div", class_="item_current_price"):
#     print(price)
#     print(price.attrs["data-price"])


        # -- Парсинг --

# {
#     "id": 4,
#     "name": "Ривьера Компакт 3600 СК \"Комби\" светло-серый/черный",
#     "image": "http://localhost:8000/media/photo/71_QhvXdTw.png",
#     "manufacturer": {
#         "id": 2,
#         "name": "Мастер лодок",
#         "description": "г. Уфа"
#     },
#     "price": 59560,
#     "product_abs_url": "/slan-keel/lodka-rivera-3600-kilevoe-naduvnoe-dno-kombi-svetlo-seryjchernyj",
#     "sale": 0,
#     "color": {
#         "id": 1,
#         "name": "Светло-серый/Чёрный"
#     },
#     "category": 13,
#     "slug": "lodka-rivera-3600-kilevoe-naduvnoe-dno-kombi-svetlo-seryjchernyj",
#     "parse_url": "https://master-lodok.ru/catalog/lodki/rivera/rivera_kompakt/rivera_kompakt_3600_sk_kombi_svetlo_seryy_chernyy_/"
# }
