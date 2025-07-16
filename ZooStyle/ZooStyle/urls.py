from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts_app/", include("accounts_app.urls", namespace="accounts_app")),
    path("grooming_app/", include("grooming_app.urls", namespace="grooming_app")),
    path("shop_app/", include("shop_app.urls", namespace="shop_app")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)