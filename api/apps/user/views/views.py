from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.apps.user.models import User
from api.apps.user.serializers import UserSerializer


class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        permission_classes = [IsAuthenticated]

        user = get_user_model()
        try:
            user = User.objects.get(id=id)
        except user.DoesNotExist:
            return Response({
                "error": "User does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)

        if user != request.user:
            return Response({
                "error": "You are not authorized to update this user"
            }, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveView(APIView):
    def get(self, reqeust, *args, **kwargs):
        id = kwargs.get('id')
        permission_classes = [IsAuthenticated]

        try:
            user = User.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response(
                {'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_deleted:
            return Response(
                {'error': 'User has been deleted'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        permission_classes = [IsAuthenticated]

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        #TODO: Implement soft delete
        permission_classes = [IsAuthenticated]

        try:
            user = User.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response(
                {'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user != request.user:
            return Response({
                "error": "You are not authorized to delete this user"
            }, status=status.HTTP_403_FORBIDDEN)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
