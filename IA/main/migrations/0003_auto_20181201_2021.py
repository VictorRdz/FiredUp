# Generated by Django 2.1.3 on 2018-12-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181201_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='departamento',
            field=models.CharField(max_length=50),
        ),
    ]