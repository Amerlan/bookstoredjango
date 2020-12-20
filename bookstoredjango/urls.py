from django.contrib import admin
from django.urls import path
from shop.views import *


urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('shop', BookListView.as_view()),
    path('product-detail/<int:pk>', BookDetailView.as_view()),
    path('update_cart', updateCart),
    path('cart', show_cart),
    path('checkout', show_checkout),
    path('checkout-order', checkout_order, name='process')
]
