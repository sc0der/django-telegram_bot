API_TOKEN = "1864593736:AAGnOmd87-dQWSdVYEEpxpyNGVcik74Ap6k"

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


category_urls = {
    "category_list": host + 'category/all',
    "category": host + 'category/', # + <category_slug>
    "products_by_category": host + 'products/category/' # + <category_slug>
}