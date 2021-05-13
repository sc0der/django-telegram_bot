import requests
from config import(
    category_urls, 
    members_urls, 
    products_urls
)
from middleware import Middleware

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
    def __init__(self, urls):
        self.urls = urls

    def get_category_list(self):
        category_list = []
        response = requests.get(url=self.urls['category_list'])
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
        response = requests.get(url=self.urls['products_by_category']+value)
        result = response.json()
        for product in result['products_by_category']:
            product_list.append(
                Product(
                    name = product['product_name'], 
                    slug = product['product_slug'], 
                    price = product['price'], 
                    category = product['category_id'], 
                )
            )
        return product_list

    def get_category_by_id(self, value):
        response = requests.get(url=self.urls['category']+value)
        category = response.json()
        return Category(
            name=category['category_name'],
            slug=category['category_slug'],
            image=category['category_image'],
        )

class FetchProduct(object):
    def __init__(self, urls):
        self.urls = urls

    def get_product_list(self):
        product_list = []
        response = requests.get(url=self.urls['product_list'])
        result = response.json()
        for product in result["products"]: 
            product_list.append(
                Product(
                    name = product['product_name'], 
                    slug = product['product_slug'], 
                    price = product['price'], 
                    category = product['category_id'], 
                )
            )
        return product_list

    def get_product_by_id(self, value):
        response = requests.get(url=self.urls['product']+value)
        product = response.json()
        return Product(
            name = product['product_name'], 
            slug = product['product_slug'], 
            price = product['price'], 
            category = product['category_id'], 
        )


class MemberObject(object):
    def __init__(self, username, id):
        self.id = id,
        self.username = username,

class Member(object):
    def __init__(self, urls, message):
        self.urls = urls
        self.message = message

    def add_new_member(self):
        if Middleware(self.message).is_bot():
            return "you are a bot. You can not to join"
            print("this is bot")
        else:
            print("username: ", self.message.from_user.first_name)
            member = {
                "id":1,
                "memberID": self.message.from_user.id,
                "mName": self.message.from_user.username if self.message.from_user.username != None else self.message.from_user.first_name
            }
            response = requests.post(
                url=self.urls['add_member'],
                data=member
            )
            result = response.json()
            return result




if __name__ == "__main__":
    testFetchCategory = FetchCategory(category_urls)
    categ_list = testFetchCategory.get_category_list()
    testFetchCategory.get_products_to_category(categ_list[0].slug)

    testProduct = FetchProduct(products_urls)
    pr1 = testProduct.get_product_list()
    print(testProduct.get_product_by_id(pr1[0].slug).slug)

