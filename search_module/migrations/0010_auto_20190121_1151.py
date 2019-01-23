# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0009_auto_20190121_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducatorRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='search_module.Student')),
            ],
        ),
        migrations.CreateModel(
            name='InstituteAffilation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affilation', to='search_module.Student')),
            ],
        ),
        migrations.AddField(
            model_name='iueducationdetails',
            name='educator_role',
            field=models.ManyToManyField(related_name='educator_role', to='search_module.EducatorRole'),
        ),
        migrations.AddField(
            model_name='iueducationdetails',
            name='institution_affilation',
            field=models.ManyToManyField(related_name='institution_affolation', to='search_module.InstituteAffilation'),
        ),
    ]