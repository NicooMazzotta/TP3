# Generated by Django 4.2.2 on 2023-06-27 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=30)),
                ('Nombre_usuario', models.CharField(max_length=20)),
                ('contrasenia', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inicio.usuario')),
                ('Direccion_tienda', models.CharField(max_length=20)),
                ('Objetos_vendidos', models.ManyToManyField(to='inicio.objeto')),
            ],
            bases=('inicio.usuario',),
        ),
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inicio.usuario')),
                ('Direccion_entregas', models.CharField(max_length=20)),
                ('Objetos_comprados', models.ManyToManyField(to='inicio.objeto')),
            ],
            bases=('inicio.usuario',),
        ),
    ]