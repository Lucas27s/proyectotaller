# Generated by Django 4.2.1 on 2023-06-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptaller', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipo_contacto',
            field=models.IntegerField(choices=[[0, 'Reclamo'], [1, 'Sugerencia'], [2, 'Felicitaciones']]),
        ),
    ]