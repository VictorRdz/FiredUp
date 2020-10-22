# Generated by Django 2.1.3 on 2018-12-02 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181201_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma_Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Idioma')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Idioma_Vacante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Idioma')),
                ('vacante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Vacante')),
            ],
        ),
    ]
