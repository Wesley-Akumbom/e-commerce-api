from django.db import models

from api.apps.category.models import Category
from api.apps.store.models import Store


class ProductManager(models.Manager):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    stores = models.ManyToManyField(Store, related_name='products')
    categories = models.ManyToManyField(Category, related_name="products")

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
