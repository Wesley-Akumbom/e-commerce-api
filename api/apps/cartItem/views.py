from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.apps.cart.models import Cart
from api.apps.cartItem.models import CartItem
from api.apps.cartItem.serializers import CartItemSerializer
from api.apps.core.permissions.permissions import IsCartOwner


class CreateItemView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def post(self, request, cart_id):
        try:
            cart = Cart.objects.get(id=cart_id)
            cart_item = CartItem.objects.filter(
                cart=cart, product_id=request.data['product_id'])
            if cart_item.exists():
                return Response({
                    "error": "Product already exists in cart"
                }, status=status.HTTP_403_FORBIDDEN)

            serializer = CartItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(cart=cart)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response({
                "error": "Cart does not exist"
            }, status=status.HTTP_404_NOT_FOUND)


class UpdateItemView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def put(self, request, id):
        try:
            cartItem = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(cartItem, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RetrieveITemView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def get(self, request, id):
        try:
            cartItem = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(cartItem)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ListItemsView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def get(self, request):
        cartItems = CartItem.objects.all()
        serializer = CartItemSerializer(cartItems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteItemView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def delete(self, request, id):
        try:
            cartItem = CartItem.objects.get(id=id)
            cartItem.delete()
            return Response({"message": f"{cartItem.product.name} deleted"}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DeleteAllItemsView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def delete(self, request):
        cartItems = CartItem.objects.all()
        cartItems.delete()
        return Response({"message": "All items deleted"}, status=status.HTTP_204_NO_CONTENT)
