# Generated by Django 2.2.7 on 2019-12-03 12:30

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0004_persona_escliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.Comuna')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.Provincia')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.Region')),
            ],
        ),
        migrations.AddField(
            model_name='provincia',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.Region'),
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
                ('tipo_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.TipoInmueble')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.Inmueble')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.Provincia'),
        ),
    ]