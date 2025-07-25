from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
    
    path("admin/", admin.site.urls),
    
    path("accounts/", include("accounts_app.urls", namespace="accounts_app")),
    path("grooming/", include("grooming_app.urls", namespace="grooming_app")),
    path("shop/", include("shop_app.urls", namespace="shop_app")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)