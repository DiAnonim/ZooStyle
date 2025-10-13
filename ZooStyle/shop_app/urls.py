from django.urls import path
from shop_app.views import ShopHomePage

app_name = 'shop_app'

urlpatterns = [
    path("home/", ShopHomePage.as_view(), name="shop_home")
]