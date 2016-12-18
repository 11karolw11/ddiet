from django.forms import ModelForm, Select
from ddiet.models import Product, ProductCategory

import django
class ProductForm(ModelForm):
    class Meta:
        from django.core.cache import cache
        cache.clear()
        model = Product
        fields = ['name', 'category', 'typical_amount', 'carbs', 'fat', 'protein', 'item_coefficient', 'ml_coefficient']