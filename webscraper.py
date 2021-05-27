from bs4 import BeautifulSoup
import requests
import json

url = 'https://dev-test.hudsonstaging.co.uk/'
response = requests.get(url, timeout = 5)
products = BeautifulSoup(response.content, "html.parser")


productArr = []

for product in products.findAll('div', attrs = {"class" : "product-tile"}):
    productObject = {
        "product" : product.find('p', attrs ={"class": "product-name"}).text,
        "metadata":{
            "image_url": product.find('img')['src'],
            "quantity": product.select_one("div.details > p").text.strip("Quantity: "),
            "price": product.select_one("div.details > p").find_next_sibling().text.strip("Price: $")
        }
    }
    productArr.append(productObject)

with open('productData.json', 'w') as outfile:
    json.dump(productArr, outfile, indent=4)



