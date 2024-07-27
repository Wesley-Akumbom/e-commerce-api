from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer
from ..core.permissions.permissions import IsStoreOwner


# Create your views here.
class ProductCreateView(APIView):

    permission_classes = [IsAuthenticated, IsStoreOwner]
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            product = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsStoreOwner]

    def patch(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": f"No Product With - {id}"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": f"No Product with id - {id}"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsStoreOwner]

    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": f"No Product with id - {id}"
            }, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message": f"Product - {product.name} deleted "}, status=status.HTTP_204_NO_CONTENT)


class ProductDeleteAllView(APIView):
    permission_classes = [IsAuthenticated, IsStoreOwner]

    def delete(self, request):
        products = Product.objects.all()
        products.delete()
        return Response({"message": "All products deleted"}, status=status.HTTP_204_NO_CONTENT)
