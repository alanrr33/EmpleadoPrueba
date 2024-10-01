from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.
class Habilidades(models.Model):
    TRABAJO_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )
    habilidad = models.CharField('Habilidad',max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + ' - ' + self.habilidad

class Empleado (models.Model):
    TRABAJO_CHOICES = (
        ('0','Contador'),
         ('1','Administrador'),
         ('2','Economista'),
         ('3','Otro')
    )

    nombre = models.CharField('Nombre',max_length=30)
    apellido = models.CharField('Apellido',max_length=30)
    nombre_completo = models.CharField('Nombre Completo', max_length=60,blank=True)
    trabajo = models.CharField('Trabajo', max_length=2,choices=TRABAJO_CHOICES)
    nrodoc = models.CharField('Nro Doc',max_length=10)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar',upload_to='empleado',blank=True,null=True)
    habilidades = models.ManyToManyField(Habilidades)
    resumen = RichTextField()

    class Meta:
        #verbose_name='' nombre singular
        #verbose_name_plural='' nombre plural
        ordering = ['nombre','apellido']
        unique_together = ('nombre','apellido','nrodoc') #constraint para combinatoria unica


    def __str__(self):
        return self.nrodoc + ' - ' + self.nombre + ' - ' + self.apellido