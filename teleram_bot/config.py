API_TOKEN = ""
host = "http://localhost:8000/"


products_urls = {
    "add_product": host + 'product/add',
    "product_list": host + 'product/all',
    "product":host + 'product/' , # + <product_slug>
    "product_images": host + "product/image/"
}

members_urls = {
    "add_member": host + 'member/add',
    "member_list": host + 'member/all',
}

cart_urls = {
    "cart_add": host + 'cart/add',
    "cart_list": host + 'cart/all',
}

cart_items_urls = {
    "cart_item_add": host + 'cart_item/add',
    "cart_item": host + 'cart_item/', # + <cItem_id>
}

order_urls = {
    "order_add": host + 'order/add',
    "order_list": host + 'order/all' 
}

category_urls = {
    "category_list": host + 'category/all',
    "category": host + 'category/', # + <category_slug>
    "products_by_category": host + 'products/category/' # + <category_slug>
}

message_urls = {
    "messages" : host+"messages/all",
    "message" : host+"messages/detail"
}
