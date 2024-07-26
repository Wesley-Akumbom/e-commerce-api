from rest_framework import serializers

from api.apps.cart.models import Cart
from api.apps.cartItem.serializers import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
