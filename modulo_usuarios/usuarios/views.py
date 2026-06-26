from tempfile import template

from django.http import HttpResponse, request 
from django.shortcuts import render  
from django.template import context, loader 

from .models import Usuario

def inicio(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())

def registros(request):
    usuarios = Usuario.objects.all()
    return render(request, 'registros.html', {'registros_html': usuarios})