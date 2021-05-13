import requests
from config import LINKS

class Category(object):
    def __init__(self, name, slug, image):
        self.name = name
        self.slug = slug
        self.image = image

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

    def test(self, value):
        print(value)

if __name__ == "__main__":
    testFetch = FetchCategory(LINKS['category_list'])
    testFetch.get_category_list()