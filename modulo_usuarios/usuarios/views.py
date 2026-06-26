from django.http import HttpResponse # type: ignore
from django.template import loader # type: ignore

def saludar(request):
    template = loader.get_template('saludar.html')
    return HttpResponse(template.render())