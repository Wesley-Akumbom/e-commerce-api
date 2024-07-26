from django.core.exceptions import ObjectDoesNotExist

from .serializers import StoreSerializer
from .models import Store
from api.apps.core.permissions.permissions import IsStoreOwner, IsSystemAdmin

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema


class CreateStoreView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = StoreSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateStoreView(APIView):
    permission_classes = [IsAuthenticated, IsStoreOwner]

    def put(self, request, id):

        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": "Store does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = StoreSerializer(store, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")

        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": "Store does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = StoreSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StoreListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StoreDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsSystemAdmin]

    def delete(self, request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({
                "error": "Store does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        store.delete()

        return Response({"message": f"Store - {store.name} deleted"}, status=status.HTTP_204_NO_CONTENT)
