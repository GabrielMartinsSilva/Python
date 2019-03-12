from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(clientes_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
