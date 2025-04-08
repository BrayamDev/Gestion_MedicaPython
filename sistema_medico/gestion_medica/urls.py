from django.urls import path
from . import views

urlpatterns = [
    path('CitaMedica/', views.citaMedicaIndex, name='CitaMedica'),
    path('', views.lista_citas_medicas, name='citas_medicas'),
]