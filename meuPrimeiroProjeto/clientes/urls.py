from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import lista_de_pessoas
from .views import persons_new
from .views import persons_update
from .views import persons_delete




urlpatterns = [

    path('list/', lista_de_pessoas, name="lista_de_pessoas"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)