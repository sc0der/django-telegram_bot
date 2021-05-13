import requests
from config import LINKS

class Category(object):
    def __init__(self, name, slug, image):
        self.name = name
        self.slug = slug
        self.image = image

class Product(object):
    def __init__(self, name, slug, price, category):
        self.name = name,
        self.slug = slug
        self.price = price
        self.category = category


        

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
        return category_list

    def get_products_to_category(self, value):
        product_list = []
        

if __name__ == "__main__":
    testFetch = FetchCategory(LINKS['category_list'])
    testFetch.get_category_list()