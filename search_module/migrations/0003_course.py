# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-05 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0002_auto_20190204_0628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=5)),
                ('course_desc', models.CharField(max_length=255)),
                ('course_subject_code', models.CharField(max_length=10)),
                ('course_catlog_number', models.PositiveIntegerField()),
                ('course_official_grade_code', models.CharField(max_length=4)),
                ('term', models.CharField(max_length=100)),
                ('campus_instrucation', models.CharField(max_length=100)),
                ('instructor', models.CharField(max_length=100)),
                ('enroll', models.CharField(max_length=100)),
                ('pending_enrollment', models.CharField(max_length=20)),
                ('calculated_remaining', models.CharField(max_length=100)),
                ('no_of_drop', models.CharField(max_length=100)),
                ('no_of_withdrawals', models.CharField(max_length=100)),
                ('campus', models.CharField(max_length=100)),
                ('class_number', models.CharField(max_length=100)),
                ('total_seats', models.PositiveIntegerField()),
                ('enrollment', models.CharField(max_length=20)),
                ('pending_enroll', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=20)),
                ('sectioin', models.CharField(max_length=20)),
                ('course_status', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'course',
            },
        ),
    ]
