# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-07 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name_plural': 'User Management'},
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff User'),
        ),
    ]
