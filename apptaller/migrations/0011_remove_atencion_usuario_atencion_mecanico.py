# Generated by Django 4.2.1 on 2023-06-29 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apptaller', '0010_atencion_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atencion',
            name='usuario',
        ),
        migrations.AddField(
            model_name='atencion',
            name='mecanico',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='apptaller.mecanico'),
            preserve_default=False,
        ),
    ]