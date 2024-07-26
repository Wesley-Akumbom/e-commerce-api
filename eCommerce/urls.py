from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('api.apps.user.urls.auth_urls')),
    path('api/users/', include('api.apps.user.urls.urls')),
    path('api/stores/', include('api.apps.store.urls')),
    path('api/categories/', include('api.apps.category.urls')),
    path('api/products/', include('api.apps.product.urls')),
    path('api/cart/', include('api.apps.cart.urls')),
    path('api/cart-items/', include('api.apps.cartItem.urls')),
    path('api/order/', include('api.apps.order.urls')),
    path('', include('eCommerce.swagger.urls'))
]
