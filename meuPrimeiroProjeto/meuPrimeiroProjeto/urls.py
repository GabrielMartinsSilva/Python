


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import hello
from .views import articles
from .views import fname2



urlpatterns = [
    path('hello/', hello),
    path('admin/', admin.site.urls),
    path('articles/<int:year>/', articles),
    path('nome/<str:nome>/', fname2)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
