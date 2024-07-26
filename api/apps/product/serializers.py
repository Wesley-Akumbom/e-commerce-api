from rest_framework import serializers
from .models import Product, Store
from ..category.models import Category
from ..category.serializers import CategorySerializer
from ..store.serializers import StoreSerializer


class ProductSerializer(serializers.ModelSerializer):
    stores = StoreSerializer(many=True, read_only=True)
    store_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Store.objects.all(),
                                                   write_only=True, source='stores')
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all(),
                                                      write_only=True, source='categories')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'unit_price', 'quantity',
                  'store_ids', 'stores', 'category_ids', 'categories']
