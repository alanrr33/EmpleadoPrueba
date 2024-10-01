from django.urls import path
from . import views

app_name='Departamento_App'

urlpatterns = [
    path('add-empleado/',views.NewDepartamentoView.as_view(),name='nuevo-depto'),
    path('listar-departamentos/',views.ListAllDepartamentosView.as_view(),name="listar-departamentos")
]
