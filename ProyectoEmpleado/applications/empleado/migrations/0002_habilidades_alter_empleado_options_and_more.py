# Generated by Django 5.1.1 on 2024-09-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['nombre', 'apellido']},
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('nombre', 'apellido', 'nrodoc')},
        ),
    ]
