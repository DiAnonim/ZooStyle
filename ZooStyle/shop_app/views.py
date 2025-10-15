from django.shortcuts import render
from django.views.generic import ListView, View

from django.http import JsonResponse
from django.template.loader import render_to_string

from shop_app.models import Category, Product


class ShopHomePage(ListView):
    model = Category
    template_name = "shop_app/shope_home.html"
    context_object_name = "categories"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
    
    
class FilterProductsView(View):
    def get(self, request, *args, **kwargs):
        category_id = request.GET.get("category_id")
        products = Product.objects.all()
        
        if category_id:
            try:
                products = products.filter(category_id=category_id)
            except ValueError:
                products = Product.objects.none()
                
        products_html = render_to_string(
            'shop_app/_product_cards.html',
            {"products": products},
            request=request
        )
        
        return JsonResponse({'products_html': products_html})

