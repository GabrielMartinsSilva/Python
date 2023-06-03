from django.urls import path
from .views import home, HomePageView
from django.contrib.auth import views as auth_views
from gestao_clientes import urls as urls_clientes
from django.views.generic.base import TemplateView





urlpatterns = [
    path('', home, name="home"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home2/', TemplateView.as_view(template_name="home2.html")),
    path('home3/', HomePageView.as_view(template_name="home3.html")),
]


#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
