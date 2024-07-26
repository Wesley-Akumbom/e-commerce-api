from django.db import models

from api.apps.cart.models import Cart
from api.apps.cartItem.models import CartItem
from api.apps.core.models import BaseModel
from api.apps.user.models import User


class Order(BaseModel, models.Model):
    STATUS_CHOICES = (
        ("P", "PENDING"),
        ("D", "DELIVERED"),
        ("C", "CANCELLED")
    )

    class ObjectManager(models.Manager):
        pass

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_quantity = models.PositiveIntegerField(default=0.00)
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(CartItem, related_name="orders")
    cart = models.OneToOneField(Cart, related_name="orders", on_delete=models.CASCADE, default=None)

    objects = ObjectManager()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order by {self.user.name}"