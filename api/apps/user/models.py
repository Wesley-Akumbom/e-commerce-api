from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from api.apps.core.models import BaseModel
# from api.apps.core.models import SoftDeleteManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Please provide an email address")

        extra_fields.setdefault('role', 'customer')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(BaseModel, AbstractUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('owner', 'OWNER'),
        ('customer', 'CUSTOMER'),
    )

    GENDER_CHOICES = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER'),
    )

    # objects = SoftDeleteManager()

    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    contact = models.CharField(max_length=20)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
