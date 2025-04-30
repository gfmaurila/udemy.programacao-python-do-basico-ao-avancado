
# Exemplo de view Django (para usar dentro de um projeto Django)

from django.http import HttpResponse

def minha_view(request):
    return HttpResponse("Olá, Django!")
