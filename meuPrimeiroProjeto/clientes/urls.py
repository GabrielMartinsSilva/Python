from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import lista_de_pessoas




urlpatterns = [
    path('list/', lista_de_pessoas),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)