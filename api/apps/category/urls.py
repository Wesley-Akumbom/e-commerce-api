from django.urls import path
from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryRetrieveView,
    CategoryUpdateView,
)

urlpatterns = [
    path('create', CategoryCreateView.as_view(), name='create-category'),
    path('update/<int:id>', CategoryUpdateView.as_view(), name='update-category'),
    path('', CategoryListView.as_view(), name='list-categories'),
    path('<int:id>', CategoryRetrieveView.as_view(), name='retrieve-category'),
    path('delete/<int:id>', CategoryDeleteView.as_view(), name='delete-category'),
]
