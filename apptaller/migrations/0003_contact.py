# Generated by Django 4.2.1 on 2023-06-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptaller', '0002_atencion_foto_mecanico_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('tipo_contacto', models.IntegerField(choices=[[0, 'Reclamo'], [1, 'Sugerencia'], [2, 'Felicitaciónes']])),
                ('mensaje', models.TextField()),
            ],
        ),
    ]