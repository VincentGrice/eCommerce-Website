# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-15 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]
