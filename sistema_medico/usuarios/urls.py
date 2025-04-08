from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarioIndex, name='UsuarioIndex'),
]
