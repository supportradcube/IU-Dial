# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-15 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0004_auto_20190107_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='permanent_postal_code',
            field=models.CharField(max_length=6),
        ),
    ]