from rest_framework import serializers

from api.apps.cartItem.models import CartItem
from api.apps.cartItem.serializers import CartItemSerializer
from api.apps.order.models import Order
from api.apps.product.models import Product
from api.apps.user.serializers import UserSerializer


class OrderItemInputSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),
                                                    source="product")
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemInputSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_amount', 'total_quantity', 'status']
        read_only_fields = ['user', 'total_amount', 'total_quantity', 'status']

    def create(self, validated_data):
        user = self.context['request'].user
        cart = user.cart
        items_data = validated_data.pop('items')

        order = Order.objects.create(user=user, cart=cart)
        total_quantity = 0
        total_amount = 0.0

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']

            cart_item = CartItem.objects.get(cart=cart, product=product)
            if quantity > cart_item.quantity:
                raise serializers.ValidationError(
                    f"Quantity for product {product.name} exceeds the quantity in the cart."
                )

            order.cart_ppitems.add(cart_item)
            total_quantity += quantity
            total_amount += quantity * product.price

        order.total_quantity = total_quantity
        order.total_amount = total_amount
        order.save()

        return order
