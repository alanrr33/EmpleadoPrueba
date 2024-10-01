from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField('Nombre',max_length=50, unique=True)
    nombre_corto = models.CharField ('Nombre Corto',max_length=20,unique=True)
    vigente = models.BooleanField('Vigente',default=True)

    class Meta:
        #verbose_name='' nombre singular
        #verbose_name_plural='' nombre plural
        ordering = ['nombre']
        unique_together = ('nombre','nombre_corto') #constraint para combinatoria unica




    def __str__(self):
        return str(self.id) + ' - ' + self.nombre + ' - ' + self.nombre_corto
