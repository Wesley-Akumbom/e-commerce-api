from django.urls import path
from .views import (
    OrderCreateView,
    OrderUpdateView,
    OrderListView,
    OrderRetrieveView,
    OrderDeleteView,
    OrderDeleteAllView
)

urlpatterns = [
    path('create', OrderCreateView.as_view(), name='create-order'),
    path('update/<int:id>', OrderUpdateView.as_view(), name='update-order'),
    path('<int:id>', OrderRetrieveView.as_view(), name='get-order'),
    path('list', OrderListView.as_view(), name='get-all-orders'),
    path('delete/<int:id>', OrderDeleteView.as_view(), name='delete-order'),
    path('delete-all', OrderDeleteAllView.as_view(), name='delete-all-orders')
]