# Generated by Django 4.2.1 on 2023-07-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptaller', '0017_alter_mecanico_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecanico',
            name='vigente',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
