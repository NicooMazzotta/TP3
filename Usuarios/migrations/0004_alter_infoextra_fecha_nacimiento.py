# Generated by Django 4.2.2 on 2023-07-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_infoextra_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoextra',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
