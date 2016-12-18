"""
Controlling data for day table
"""
import json
from django.core.serializers.json import DjangoJSONEncoder
from ddiet import models


class DayTable():
    def __init__(self, date):
        self.date = date

    def get_products(self):
        products = models.ProductData.objects.filter(eat_date__gte=self.date).values('product', 'amount')
        js_products = []
        for row in products:
            product = models.Product.objects.get(pk=row['product'])
            amount = float(row['amount'])
            js_pr = {'Product' : product.name,
                     'Amount'  : row['amount'],
                     'Carbs'   :  str(product.carbs * amount / 100.0),
                     'Fat'     :  str(product.fat * amount / 100.0),
                     'Protein' :  str(product.protein * amount / 100.0),
                     'Kcal'    :  str((amount / 100.0) * (4 * product.carbs + 9 * product.fat + 4 * product.protein)),
                     'Valuable':  "true"}
            js_products.append(js_pr)
        #todo sum in different structure, use queries instead of manual sum
        js_sum = {'Product' : 'Sum',
                  'Amount'  : str(sum(int(p['Amount']) for p in js_products)),
                  'Carbs'   : str(sum(float(p['Carbs']) for p in js_products)),
                  'Fat'     : str(sum(float(p['Fat']) for p in js_products)),
                  'Protein' : str(sum(float(p['Protein']) for p in js_products)),
                  'Kcal'    : str(sum(int(float(p['Kcal'])) for p in js_products)),
                  'Valuable':  "false"}
        js_products.append(js_sum)
        return json.dumps(js_products, cls=DjangoJSONEncoder)

