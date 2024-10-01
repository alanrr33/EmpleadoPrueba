from django import forms
from .models import Empleado
from applications.departamento.models import Departamento

class UpdateEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre','apellido','trabajo',
                  'departamento','habilidades','avatar')

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido',
                    'class': 'form-control'
                }
            ),
            'trabajo': forms.Select(
                attrs={
                    'placeholder': 'Trabajo',
                    'class': 'form-control'
                }
            ),
            'departamento': forms.Select(
                attrs={
                    'placeholder': 'Departamento',
                    'class': 'form-control'
                }
            ),
            'habilidades': forms.SelectMultiple(
                attrs={
                    'placeholder': 'Habilidades',
                    'class': 'form-control'
                }
            ),
            'avatar': forms.FileInput(
                attrs={
                    'placeholder': 'Avatar',
                    'class': 'form-control'
                }
            )
        }

class CreateEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre','apellido','nrodoc','trabajo',
                  'departamento','habilidades','avatar')

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido',
                    'class': 'form-control'
                }
            ),
            'nrodoc': forms.TextInput(
                attrs={
                    'placeholder': 'Número Documento',
                    'class': 'form-control'
                }
            ),
            'trabajo': forms.Select(
                attrs={
                    'placeholder': 'Trabajo',
                    'class': 'form-control'
                }
            ),
            'departamento': forms.Select(
                attrs={
                    'placeholder': 'Departamento',
                    'class': 'form-control'
                }
            ),
            'habilidades': forms.SelectMultiple(
                attrs={
                    'placeholder': 'Habilidades',
                    'class': 'form-control'
                }
            ),
            'avatar': forms.FileInput(
                attrs={
                    'placeholder': 'Avatar',
                    'class': 'form-control'
                }
            )
        }