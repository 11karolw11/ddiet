from ddiet import models
import json
from django.core.serializers.json import DjangoJSONEncoder


class Products:
    @staticmethod
    def calculate_macro(prodName, amount):
        try:
            product = models.Product.objects.get(name=prodName)
            coeff = float(amount) / 100.0
            rv = { "Carbs"   : '%.1f' % (product.carbs * coeff),
                   "Fat"     : '%.1f' % (product.fat * coeff),
                   "Protein" : '%.1f' % (product.protein * coeff),
                   "Kcal"    : '%.1f' % (coeff * (4 * product.carbs + 9 * product.fat + 4 * product.protein)) }
            return json.dumps(rv, cls=DjangoJSONEncoder)
        except models.Product.DoesNotExist:
            return None