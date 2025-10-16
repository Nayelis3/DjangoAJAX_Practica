from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import Estado

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
