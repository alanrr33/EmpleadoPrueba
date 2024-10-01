# Generated by Django 5.1.1 on 2024-09-08 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_alter_departamento_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('trabajo', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Otro')], max_length=2, verbose_name='Trabajo')),
                ('nrodoc', models.CharField(max_length=10, verbose_name='Nro Doc')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
            ],
        ),
    ]
