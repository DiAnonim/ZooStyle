from django.urls import path
from shop_app.views import ShopHomePage, FilterProductsView

app_name = 'shop_app'

urlpatterns = [
    path("home/", ShopHomePage.as_view(), name="shop_home"),
    path('filter-products/', FilterProductsView.as_view(), name='filter_products'),
]