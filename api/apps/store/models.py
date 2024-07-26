from django.db import models

from api.apps.core.models import BaseModel
from api.apps.user.models import User


class StoreManager(models.Manager):
    pass


class Store(BaseModel, models.Model):
    name = models.CharField(max_length=255)
    store_email = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = StoreManager()

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name


