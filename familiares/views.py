from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import familiares


def listar_familiares(request):
    queryset = familiares.objects.all()
    diccionario = {'familiares': queryset}
    plantilla = loader.get_template('lista_familiares.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)