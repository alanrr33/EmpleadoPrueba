from django import forms
from .models import Departamento

"""class NewDepartamentoForm(forms.Form):
    empleado_nombre = forms.CharField(max_length=30,required=True)
    empleado_apellido = forms.CharField(max_length=30,required=True)
    empleado_nrodoc = forms.CharField(max_length=10,required=True)
    departamento_nombre = forms.CharField(max_length=50, required=True)
    departamento_nombre_corto = forms.CharField(max_length=20, required=True)
"""


class CreateDepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('nombre', 'nombre_corto')

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                    'class': 'form-control'
                }
            ),
            'nombre_corto': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre Corto',
                    'class': 'form-control'
                }
            )

        }
