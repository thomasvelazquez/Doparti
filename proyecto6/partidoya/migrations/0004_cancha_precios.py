# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partidoya', '0003_jugador_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancha',
            name='precios',
            field=models.CharField(default='no data', max_length=200),
            preserve_default=False,
        ),
    ]
