from django.urls import path
from .views import (
    CreateCartView,
    CartRetrieveView,
    CartDeleteView,
    UpdateCartView
)


urlpatterns = [
    path('create', CreateCartView.as_view(), name='create-cart'),
    path('update/<int:id>', UpdateCartView.as_view(), name='update-view'),
    path('<int:id>', CartRetrieveView.as_view(), name='get-cart'),
    path('delete/<int:id>', CartDeleteView.as_view(), name='delete-cart'),
]