# Generated by Django 4.2.2 on 2023-07-13 17:41

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('descripcion', ckeditor.fields.RichTextField(null=True)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='imagen')),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('en_venta', models.BooleanField(default=True)),
                ('comprador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compras', to=settings.AUTH_USER_MODEL)),
                ('vendedor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
