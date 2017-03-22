from ddiet import models
import json
from django.core.serializers.json import DjangoJSONEncoder


class Products:
    @staticmethod
    def date_jquery_to_python(j_date):
        month, day, year = str(j_date).split('/')
        return year + '-' + month + '-' + day


    @staticmethod
    def calculate_macro(product, amount):
        try:
            coeff = float(amount) / 100.0
            rv = { "Carbs"   : '%.1f' % (product.carbs * coeff),
                   "Fat"     : '%.1f' % (product.fat * coeff),
                   "Protein" : '%.1f' % (product.protein * coeff),
                   "Kcal"    : '%.1f' % (coeff * (4 * product.carbs + 9 * product.fat + 4 * product.protein)) }
            return json.dumps(rv, cls=DjangoJSONEncoder)
        except models.Product.DoesNotExist:
            return None

    @staticmethod
    def update_product_day(prod_name, date, amount):
        #XXX for some reason date is in mm/dd/yyyy format
        date = Products.date_jquery_to_python(date)
        product = models.Product.objects.get(name=prod_name)
        prod_day = models.ProductData.objects.filter(product=product, eat_date=date)
        if len(prod_day) > 0:
            prod_day[0].amount = amount
            prod_day[0].save()
        else:
            models.ProductData.objects.create(eat_date=date, product=product, amount=amount)

        return Products.calculate_macro(product, amount)