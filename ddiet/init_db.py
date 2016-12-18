"""
Create database structure.
Initialize database with base products
Execute using manage.py
"""

import pandas
from ddiet.models import ProductCategory
from ddiet.models import Product

def load_products(path):
    datagram = pandas.read_csv(path)
    categories = [category for category in datagram.columns.get_values() if not category.startswith("Unnamed")]
    return datagram, categories

def insert_category_products(datagram, category, object):
    category_ind = datagram.columns.get_loc(category)
    category_datagram = datagram.iloc[:, range(category_ind, category_ind + 5)].dropna(how='all').fillna('0')
    for product in category_datagram.to_records(index=False):
        typ_amount = int(product[1])
        multiplier = 100.0 / typ_amount
        c = float(product[2].replace(',','.')) * multiplier
        f = float(product[3].replace(',','.')) * multiplier
        p = float(product[4].replace(',','.')) * multiplier
        pr = Product(name=product[0], category=object, typical_amount=typ_amount,
                     carbs=c, fat=f, protein=p)
        pr.save()

datagram, categories = load_products("produkty.csv")

ProductCategory.objects.all().delete()
for category in categories:
    object = ProductCategory.objects.create(category_name = category)
    insert_category_products(datagram, category, object)






