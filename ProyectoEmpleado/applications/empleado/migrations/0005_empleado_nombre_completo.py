# Generated by Django 5.1.1 on 2024-09-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0004_empleado_resumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='nombre_completo',
            field=models.CharField(blank=True, max_length=60, verbose_name='Nombre Completo'),
        ),
    ]
