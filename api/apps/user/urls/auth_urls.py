from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from api.apps.user.views.auth_views import (
    CreateUserView,
    CheckAuthenticationView,
    ChangePasswordView
)

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logged-in/', CheckAuthenticationView.as_view(), name='check_authentication'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password')
]