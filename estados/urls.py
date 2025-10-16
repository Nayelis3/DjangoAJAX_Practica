from django.urls import path
from .views import (
        MunicipioAjaxView,
        formulario_estado_municipio,
        crear_estado,
        crear_municipio,
        inicio
    )

urlpatterns = [
    path('', inicio, name='inicio'),
    path('ajax/municipios/', MunicipioAjaxView.as_view(), name='ajax_municipios_por_estado'),
    path('form-estado-municipio/', formulario_estado_municipio, name='form_estado_municipio'),
    path('crear-estado/', crear_estado, name='crear_estado'),
    path('crear-municipio/', crear_municipio, name='crear_municipio'),
]