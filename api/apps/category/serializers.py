from rest_framework import serializers

from api.apps.category.models import Category
from api.apps.product.models import Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
