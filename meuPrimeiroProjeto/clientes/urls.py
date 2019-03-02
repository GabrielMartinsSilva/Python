from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import lista_de_pessoas
from .views import novas_pessoas




urlpatterns = [

    path('list/', lista_de_pessoas, name="lista_de_pessoas"),
    path('new/', novas_pessoas, name="person_new"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)