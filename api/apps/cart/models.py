from django.db import models

from api.apps.product.models import Product
from api.apps.user.models import User


class CartManager(models.Manager):
    pass


class Cart(models.Model):
    name = models.CharField(max_length=50, default="My Cart")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    objects = CartManager()

    def __str__(self):
        return self.name
