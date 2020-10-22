# Generated by Django 2.1.3 on 2018-12-02 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_idioma_usuario_idioma_vacante'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulacion',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='educacion_usuario',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Area_Educativa'),
        ),
    ]