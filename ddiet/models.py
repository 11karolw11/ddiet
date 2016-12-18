from django.db import models


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    typical_amount = models.PositiveSmallIntegerField()
    carbs = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    item_coefficient = models.FloatField(null=True, blank=True)
    ml_coefficient = models.FloatField(null=True, blank=True)

class ProductData(models.Model):
    eat_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.PositiveSmallIntegerField()