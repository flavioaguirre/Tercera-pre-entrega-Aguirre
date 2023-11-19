from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleos
from .forms import EmpleoForm


def lista_empleos(request):
    lista_empleos = Empleos.objects.all().order_by('-fecha_publicacion_empleo')
    return render(request, 'empleos/lista_empleos.html', {'lista_empleos': lista_empleos})

def publicar_empleo(request):
    if request.method == 'POST':
        empleo_form = EmpleoForm(request.POST)
        if empleo_form.is_valid():
            datos_nuevo_empleo = empleo_form.cleaned_data

            titulo = datos_nuevo_empleo.get('titulo_empleo')
            descripcion = datos_nuevo_empleo.get('descripcion_empleo')
            autor = request.user

            empleo_nuevo = Empleos(
                titulo_empleo=titulo, descripcion_empleo=descripcion, autor_empleo=autor)
            empleo_nuevo.save()
        return redirect('empleos')
    return render(request, 'empleos/publicar_empleo.html', {
            'empleo_form': EmpleoForm,
            })

def detalle_empleo(request, id):
    empleo = get_object_or_404(Empleos, pk=id)
    return render(request, 'empleos/detalle_empleo.html', {'empleo': empleo})