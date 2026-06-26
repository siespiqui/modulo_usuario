from tempfile import template

from django.http import HttpResponse, request # type: ignore
from django.shortcuts import render  # type: ignore
from django.template import context, loader  # type: ignore

from .models import Usuario

def inicio(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())

def registros(request):
    template = loader.get_template('registros.html')
    usuarios = Usuario.objects.all().values()
    context = {
        'registros_html': usuarios
    }

    return HttpResponse(template.render(context, request))