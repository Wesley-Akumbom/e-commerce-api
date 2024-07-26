from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ProductCreateView,
    ProductUpdateView,
    ProductRetrieveView,
    ProductListView,
    ProductDeleteView,
    ProductDeleteAllView
)

urlpatterns = [
    path('create', ProductCreateView.as_view(), name='create-product'),
    path('update/<int:id>', ProductUpdateView.as_view(), name='update-product'),
    path('<int:id>', ProductRetrieveView.as_view(), name='get-product'),
    path('', ProductListView.as_view(), name='list-products'),
    path('delete/<int:id>', ProductDeleteView.as_view(), name='delete-product'),
    path('delete-all', ProductDeleteAllView.as_view(), name='delete-all-products'),
]
