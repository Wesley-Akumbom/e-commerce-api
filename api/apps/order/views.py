from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.apps.core.permissions.permissions import IsCartOwner
from api.apps.order.models import Order
from api.apps.order.serializers import OrderSerializer


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def put(self, request, id):
        try:
            order = Order.objects.get(id=id)
            serializer = OrderSerializer(order, data=request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)


class OrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderRetrieveView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def get(self, id, request):
        try:
            order = Order.objects.get(id)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)


class OrderDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def delete(self, id, request):
        try:
            order = Order.objects.get(id)
            order.delete()
            return Response({"message": "Order deleted"}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)


class OrderDeleteAllView(APIView):
    permission_classes = [IsAuthenticated, IsCartOwner]

    def delete(self, request):
        orders = Order.objects.all()
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
