from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission

from api.apps.cart.models import Cart


class IsStoreOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsSystemAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsCartOwner(BasePermission):
    def has_permission(self, request, view):
        cart_id = view.kwargs.get('id') or view.kwargs.get('cart_id')

        if not cart_id:
            return False

        try:
            cart = Cart.objects.get(id=cart_id)
        except ObjectDoesNotExist:
            return False

        return cart.user == request.user
