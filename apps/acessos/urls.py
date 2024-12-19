from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrar, name="acessos.entrar"),
    path('sair', views.sair, name="acessos.sair"),
]