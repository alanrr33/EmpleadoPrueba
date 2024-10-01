from django import forms
from .models import Prueba

class PruebaForm (forms.ModelForm):


    class Meta:
        model = Prueba
        fields = ('titulo','subtitulo')
        widgets = {
            'titulo':forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese titulo'
                }
            )

        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 8:
            raise forms.ValidationError('Ingrese un titulo de más de 8 caracteres')
        return titulo
