# Generated by Django 2.1.3 on 2018-11-29 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20181128_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacante',
            name='empresa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.Empresa'),
        ),
    ]
