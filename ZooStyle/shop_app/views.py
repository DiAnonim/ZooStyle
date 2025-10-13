from django.shortcuts import render
from django.views.generic import ListView

from shop_app.models import Category, Product


class ShopHomePage(ListView):
    model = Category
    template_name = "shop_app/shope_home.html"
    context_object_name = "categories"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all
        return context
    
    

