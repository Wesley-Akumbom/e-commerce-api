from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.apps.category.models import Category
from api.apps.category.serializers import CategorySerializer
from api.apps.core.permissions.permissions import IsSystemAdmin


class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated, IsSystemAdmin]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsSystemAdmin]

    def put(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": "Category does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": "Category does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsSystemAdmin]

    def delete(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": "Category does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response({"message": f"Category deleted"}, status=status.HTTP_204_NO_CONTENT)
