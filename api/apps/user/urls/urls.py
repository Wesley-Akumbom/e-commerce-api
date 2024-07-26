from django.urls import path
from api.apps.user.views.views import (
    UpdateUserView,
    UserRetrieveView,
    UserListView,
    UserDeleteView
)

urlpatterns = [
    path('update/<int:id>/', UpdateUserView.as_view(), name='update-user'),
    path('<int:id>/', UserRetrieveView.as_view(), name='get-user'),
    path('', UserListView.as_view(), name='list-users'),
    path('delete/<int:id>/', UserDeleteView.as_view(), name='delete-user'),
]