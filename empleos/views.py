from django.shortcuts import render

def empleos(request):
    return render(request, 'empleos/lista_empleos.html', {})
