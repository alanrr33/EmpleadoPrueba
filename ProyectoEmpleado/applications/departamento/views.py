from django.shortcuts import  render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from django.contrib import messages
from .models import Departamento
from .forms import CreateDepartamentoForm
from applications.empleado.models import Empleado
from .models import Departamento

class ListAllDepartamentosView(ListView):
    template_name = 'empleado/listar-todo.html'
    model = Departamento
    paginate_by = 4
    ordering = 'nombre'
    context_object_name = 'departamentos'

    def get_queryset(self):
        kword = self.request.GET.get('kword_depto','')
        print (kword)
        lista = Departamento.objects.filter(
            nombre_corto__icontains=kword
        )
        return lista

class NewDepartamentoView(FormView):
    template_name = 'empleado/add.html'
    form_class = CreateDepartamentoForm
    success_url = reverse_lazy('Departamento_App:listar-departamentos')

    def post(self, request, *args, **kwargs):
        messages.success(request, "Departamento creado con éxito.")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print("###FORM_VALID####")

        departamento_nombre = form.cleaned_data['nombre']
        departamento_nombre_corto = form.cleaned_data['nombre_corto']

        Departamento.objects.create(
            nombre = departamento_nombre,
            nombre_corto = departamento_nombre_corto
        )
        return super(NewDepartamentoView,self).form_valid(form)