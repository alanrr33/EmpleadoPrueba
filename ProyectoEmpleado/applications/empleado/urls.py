from django.urls import path
from . import views

app_name='Empleado_App'

urlpatterns = [
    path('',views.InicioView.as_view(),name='Inicio'),
    path('listar-empleados/',views.ListAllEmpleados.as_view(), name="listar-empleados"),
    path('list-por-area/<empleado>',views.ListByArea.as_view(), name="empleados_area"),
    path('buscar-empleado/',views.ListByKeyword.as_view()),
    path('habilidades-empleado/<id>',views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view(), name="empleado_detail"),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name="add-empleado"),
    path('success/', views.SuccessView.as_view(), name='Correcto'),
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name='modificar-empleado'),
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name='borrar-empleado'),
    path('listar-empleados-admin/',views.ListAllEmpleadosAdmin.as_view(),name="listar-empleados-admin"),
]
