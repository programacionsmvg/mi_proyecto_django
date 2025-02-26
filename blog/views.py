from django.shortcuts import render

def hola_mundo(request):
    contexto = {'mensaje': 'Hola Mundo desde Django'}
    return render(request, 'index.html', contexto)


