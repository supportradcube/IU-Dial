# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-07 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherdetails',
            name='check_field',
            field=models.BooleanField(default=True),
        ),
    ]
