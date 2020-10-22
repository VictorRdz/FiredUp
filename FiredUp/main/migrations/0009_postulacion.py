# Generated by Django 2.1.3 on 2018-11-29 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_vacante_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Usuario')),
                ('vacante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Vacante')),
            ],
        ),
    ]
