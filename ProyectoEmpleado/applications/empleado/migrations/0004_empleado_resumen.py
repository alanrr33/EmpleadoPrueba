# Generated by Django 5.1.1 on 2024-09-08 17:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_empleado_avatar_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='resumen',
            field=ckeditor.fields.RichTextField(default='txt'),
            preserve_default=False,
        ),
    ]
