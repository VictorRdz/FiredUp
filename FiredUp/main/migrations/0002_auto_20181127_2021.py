# Generated by Django 2.1.3 on 2018-11-28 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacante',
            old_name='sexo',
            new_name='es_hombre',
        ),
    ]