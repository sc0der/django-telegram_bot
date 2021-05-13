import requests
host = "http://localhost:8000/"

class FetchCategory(object):
    def __init__(self, url):
        self.url = url

    def get_category_list(self, category_list=[]):
        pass


def fetch_otus_json_data():
    products = []
    url = 'http://localhost:8000/product/all'
    drf_response = requests.get(url=url)
    resp = drf_response.json()
    for prod in resp["products"]:
        products.append({"product":[ prod["product_name"], "http://localhost:8000"+str(prod["image"])]})
    print(len(products))
    return products