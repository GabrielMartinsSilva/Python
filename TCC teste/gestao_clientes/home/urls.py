from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views
from gestao_clientes import urls as urls_clientes



urlpatterns = [
    path('', home, name="home"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),



] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
