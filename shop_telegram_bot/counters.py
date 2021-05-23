from vali.counters import CounterBase
from big_shop.models import Product
class MyModelCounter(CounterBase):
    title = 'Продукты'
    def get_value(self, request):
        return Product.objects.count()
        