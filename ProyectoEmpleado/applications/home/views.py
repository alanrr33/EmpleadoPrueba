from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaFoundationView(TemplateView):
    template_name = 'home/pruebacss.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['a','b','c']
    context_object_name = 'listaprueba'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = 'home/pruebas.html'
    context_object_name = 'lista_prueba'

class ModeloPruebaCreateView(CreateView):
    model = Prueba
    template_name = 'home/add.html'
    form_class = PruebaForm
    success_url = '/'