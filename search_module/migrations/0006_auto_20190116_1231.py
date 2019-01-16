# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0005_auto_20190115_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=5)),
                ('course_desc', models.CharField(max_length=255)),
                ('course_subject_code', models.CharField(max_length=10)),
                ('course_catlog_number', models.PositiveIntegerField()),
                ('course_official_grade_code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='GrantEnrollmentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.PositiveIntegerField()),
                ('course_subject_code', models.CharField(max_length=10)),
                ('university_id', models.CharField(max_length=10)),
                ('academic_term_code', models.CharField(max_length=4)),
                ('grant_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='grant_en_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_detail', to='search_module.GrantEnrollmentData'),
        ),
    ]
