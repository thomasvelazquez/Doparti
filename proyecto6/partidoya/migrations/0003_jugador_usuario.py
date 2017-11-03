# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 13:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partidoya', '0002_remove_jugador_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
