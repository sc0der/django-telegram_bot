API_TOKEN = "1864593736:AAGnOmd87-dQWSdVYEEpxpyNGVcik74Ap6k"

host = "http://localhost:8000/"


LINKS = {
    "category_list": host + 'category/all',
    "category": host + 'category/', # + <category_slug>
    "add_product": host + 'product/add',
    "product_list": host + 'product/all',
    "product":host + 'product/' , # + <product_slug>
    "add_member": host + 'member/add',
    "member_list": host + 'member/all',
    "products_by_category": host + 'products/category/' # + <category_slug>
}