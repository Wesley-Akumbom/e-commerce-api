from django.urls import path

from .views import (
    CreateItemView,
    UpdateItemView,
    RetrieveITemView,
    ListItemsView,
    DeleteItemView,
    DeleteAllItemsView
)

urlpatterns = [
    path('create/<int:cart_id>', CreateItemView.as_view(), name='create-item'),
    path('update/<int:id>', UpdateItemView.as_view(), name='update-item'),
    path('list', ListItemsView.as_view(), name='list-items'),
    path('<int:id>', RetrieveITemView.as_view(), name='retrieve-item'),
    path('delete/<int:id>', DeleteItemView.as_view(), name='delete-item'),
    path('delete-all', DeleteAllItemsView.as_view(), name='delete-all-items'),
]
