from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import Estado
from .forms import EstadoForm, MunicipioForm

def inicio(request):
    return render(request, 'inicio.html')

class MunicipioAjaxView(View):
    def get(self, request, *args, **kwargs):
            # Verificar si la solicitud es AJAX
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            return HttpResponseBadRequest("Bad Request: not AJAX")

        estado_id = request.GET.get('estado_id')
        if not estado_id:
            return JsonResponse({"error": "estado_id no proporcionado"}, status=400)

        try:
            estado_id = int(estado_id)
        except ValueError:
            return JsonResponse({"error": "estado_id inválido"}, status=400)

        from .models import Estado  
        try:
            estado = Estado.objects.get(pk=estado_id)
        except Estado.DoesNotExist:
            return JsonResponse({"error": "Estado no encontrado"}, status=404)

        municipios_qs = estado.municipios.all().values('id', 'nombre')
        municipios = list(municipios_qs)
        return JsonResponse({"municipios": municipios})

def formulario_estado_municipio(request):
    estados = Estado.objects.all().order_by('nombre')
    return render(request, 'form_estado_municipio.html', {'estados': estados})

def crear_estado(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Estado creado correctamente.')
            return redirect('crear_estado')
        else:
            messages.error(request, '❌ Error al crear el estado.')
    else:
        form = EstadoForm()
    return render(request, 'crear_estado.html', {'form': form})


def crear_municipio(request):
    if request.method == 'POST':
        form = MunicipioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Municipio creado correctamente.')
            return redirect('crear_municipio')
        else:
            messages.error(request, '❌ Error al crear el municipio.')
    else:
        form = MunicipioForm()
    return render(request, 'crear_municipio.html', {'form': form})
