from django.shortcuts import render
from django.utils import encoding
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.apps.user.models import User
from api.apps.user.serializers import UserSerializer


class CreateUserView(APIView):
    """
    This method creates a user based on the request body
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))  # Hash the password
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckAuthenticationView(APIView):
    """
    Checks authentication status of a user
    """

    def get_token_from_header(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        return auth_header.split(' ')[1] if auth_header.startswith('Bearer ') else ''

    def get(self, request):
        token = self.get_token_from_header(request)

        jwt_authentication = JWTAuthentication()

        try:
            # Validate the token
            validated_token = jwt_authentication.get_validated_token(token)
            user = jwt_authentication.get_user(validated_token)

            return Response({'message': 'User is authenticated and token is valid.'})

        except (InvalidToken, TokenError):
            error_message = {
                'error': 'Invalid Authentication',
                'message': 'User is authenticated but token is invalid.',
                'status': status.HTTP_401_UNAUTHORIZED
            }
            return Response(error_message, status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordView(APIView):
    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({
                "message": "Password changed"
            }, status=status.HTTP_204_NO_CONTENT)

        return Response({
            "error": "Invalid old password"
        }, status=status.HTTP_400_BAD_REQUEST)

#TODO: Reset password and confirm reset password views
