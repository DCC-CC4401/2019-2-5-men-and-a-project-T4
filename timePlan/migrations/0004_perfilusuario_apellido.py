# Generated by Django 2.2.4 on 2019-12-04 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timePlan', '0003_auto_20191018_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='apellido',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]