from django.db import models

from api.apps.cart.models import Cart
from api.apps.product.models import Product


class CartItemManager(models.Manager):
    pass


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    objects = CartItemManager()

    def __str__(self):
        return f'{self.cart} - {self.product} - {self.quantity}'
