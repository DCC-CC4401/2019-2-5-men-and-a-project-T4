# Generated by Django 2.2.6 on 2019-10-18 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timePlan', '0002_auto_20191009_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='amigos',
            field=models.ManyToManyField(related_name='_perfilusuario_amigos_+', to='timePlan.PerfilUsuario'),
        ),
        migrations.AddField(
            model_name='perfilusuario',
            name='solicitudes',
            field=models.ManyToManyField(related_name='_perfilusuario_solicitudes_+', to='timePlan.PerfilUsuario'),
        ),
        migrations.AlterField(
            model_name='perfilusuario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PerfilUsuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
