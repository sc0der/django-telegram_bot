import requests



def fetch_otus_json_data():
    products = []
    url = 'http://localhost:8000/product/all'
    drf_response = requests.get(url=url)
    resp = drf_response.json()
    for prod in resp["products"]:
        products.append({"product":[ prod["product_name"], "http://localhost:8000"+str(prod["image"])]})
    print(len(products))
    return products