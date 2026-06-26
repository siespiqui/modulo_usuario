from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('saludar/', views.saludar, name='saludo'),
]