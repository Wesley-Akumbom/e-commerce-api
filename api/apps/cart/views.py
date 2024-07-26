from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.apps.cart.models import Cart
from api.apps.cart.serializers import CartSerializer
from api.apps.core.permissions.permissions import IsCartOwner


class CreateCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCartView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def put(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": "Cart does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartRetrieveView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def get(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": "Cart does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def delete(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": "Cart does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
