from rest_framework import serializers
from .models import CartItem
from ..product.models import Product
from ..product.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),
                                                    write_only=True, source='product')

    class Meta:
        model = CartItem
        fields = ['product', 'product_id', 'quantity']
