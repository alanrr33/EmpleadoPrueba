from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Empleado
from .forms import UpdateEmpleadoForm, CreateEmpleadoForm


# Create your views here.

class InicioView(TemplateView):
    # vista pagina inicio
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'empleado/listar-todo.html'
    paginate_by = 5
    ordering = 'apellido'
    context_object_name = 'empleados'

    def get_queryset(self):
        kword = self.request.GET.get('kword_empleaado', '')
        print(kword)
        lista = Empleado.objects.filter(
            nombre_completo__icontains=kword
        )
        return lista


class ListAllEmpleadosAdmin(ListView):
    template_name = 'empleado/listar-empleados-admin.html'
    paginate_by = 10
    ordering = 'apellido'
    context_object_name = 'empleados'
    model = Empleado


class ListByArea(ListView):
    template_name = 'empleado/list-por-area.html'
    paginate_by = 5
    ordering = 'nombre'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['empleado']
        lista = Empleado.objects.filter(
            departamento__nombre_corto=area.capitalize()
        )
        return lista


class ListByKeyword(ListView):
    # listar empleados por palabra clave
    template_name = 'empleado/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        print(kword)
        lista = Empleado.objects.filter(
            nombre=kword.capitalize()
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_empleado = self.kwargs['id']
        empleado = Empleado.objects.get(id=id_empleado)
        lista = empleado.habilidades.all()
        return lista


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/detalle-empleado.html'
    context_object_name = 'empleado'

    """def get_context_data(self, **kwargs):
        context = {}
        context = super().get_context_data(**context)
        context['titulo'] = 'Empleado del mes'
        print(context)
        return context"""


class SuccessView(TemplateView):
    template_name = 'empleado/success.html'


class EmpleadoCreateView(CreateView):
    template_name = 'empleado/add.html'
    model = Empleado
    form_class = CreateEmpleadoForm
    # fields = ['nombre','apellido','nrodoc','trabajo','empleado','habilidades']
    success_url = reverse_lazy('Empleado_App:listar-empleados-admin')

    def post(self, request, *args, **kwargs):
        messages.success(request, "Empleado Creado con éxito.")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.nombre_completo = empleado.nombre + ' ' + empleado.apellido
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'empleado/update.html'
    model = Empleado
    form_class = UpdateEmpleadoForm
    # fields = ['nombre', 'apellido', 'trabajo', 'empleado', 'habilidades']
    success_url = reverse_lazy('Empleado_App:listar-empleados-admin')

    def post(self, request, *args, **kwargs):
        messages.success(request, "Empleado Updateado con éxito.")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print("########METODO FORM VALID#######")
        empleado = form.save(commit=False)
        empleado.nombre_completo = empleado.nombre + ' ' + empleado.apellido
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = 'empleado/delete.html'
    model = Empleado
    success_url = reverse_lazy('Empleado_App:listar-empleados-admin')

    def post(self, request, *args, **kwargs):
        messages.success(request, "Empleado Borrado con éxito.")
        return super().post(request, *args, **kwargs)
