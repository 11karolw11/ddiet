import json

from django.test import TestCase
from django.utils import timezone

from .models import ProductData
from .models import Product
from .models import ProductCategory

from .daytable import DayTable

class DayTableTests(TestCase):
    def setUp(self):
        c1 = ProductCategory.objects.create(category_name="Wegle")
        p1 = Product.objects.create(name="Mango", category=c1, typical_amount=100, carbs="30", fat="1.0", protein="5")
        ProductData.objects.create(eat_date=timezone.now(), product=p1, amount="90")
    def test_get_products(self):
        some_product = ProductData.objects.get(pk=1)
        daytable = DayTable(some_product.eat_date)
        values = json.loads(daytable.get_products())[0]
        kcal = float(values['Carbs'])*4.0 + float(values['Fat'])*9.0 + float(values['Protein'])*4.0
        self.assertAlmostEqual(kcal, float(values['Kcal']))




