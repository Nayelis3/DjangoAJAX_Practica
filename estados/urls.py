from django.urls import path
from .views import MunicipioAjaxView, formulario_estado_municipio

urlpatterns = [
    path('ajax/municipios/', MunicipioAjaxView.as_view(), name='ajax_municipios_por_estado'),
    path('form-estado-municipio/', formulario_estado_municipio, name='form_estado_municipio'),
]