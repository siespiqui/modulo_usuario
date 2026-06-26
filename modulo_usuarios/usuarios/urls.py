from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('registros/', views.registros, name='registros')
]