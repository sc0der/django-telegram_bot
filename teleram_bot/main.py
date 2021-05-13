import requests
from config import LINKS

class Category(object):
    def __init__(self, name, slug, image):
        self.name = name
        self.slug = slug
        self.image = image
        return Category(self.name, self.slug, self.image)

class FetchCategory(object):
    def __init__(self, url):
        self.url = url

    def get_category_list(self):
        category_list = []
        response = requests.get(url=self.url)
        result = response.json()
        for category in result["categories"]: 
            category_list.append(
                Category(
                    name=category['category_name'],
                    slug=category['category_slug'],
                    image=category['category_image'],
                    )
                )
        print(len(category_list))
        return category_list

    def test(self, value):
        print(value)

if __name__ == "__main__":
    testFetch = FetchCategory("")
    testFetch.test(LINKS["all_categories"])


    


        
# def fetch_otus_json_data():
#     products = []
#     url = 'http://localhost:8000/product/all'
#     drf_response = requests.get(url=url)
#     resp = drf_response.json()
#     for prod in resp["products"]:
#         products.append({"product":[ prod["product_name"], "http://localhost:8000"+str(prod["image"])]})
#     print(len(products))
#     return products