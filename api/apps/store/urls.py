from django.urls import path
from .views import (
    CreateStoreView,
    StoreRetrieveView,
    StoreListView,
    UpdateStoreView,
    StoreDeleteView
)

urlpatterns = [
    path('create', CreateStoreView.as_view(), name='create-store'),
    path('update/<int:id>', UpdateStoreView.as_view(), name='update-store'),
    path('list', StoreListView.as_view(), name='store-list'),
    path('<int:id>', StoreRetrieveView.as_view(), name='get-store'),
    path('delete/<int:id>', StoreDeleteView.as_view(), name='delete-store'),
]
