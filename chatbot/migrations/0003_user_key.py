# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-03 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_timetable_fri_timetable_mon_timetable_thu_timetable_tue_timetable_wed'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Key', models.CharField(max_length=20)),
                ('c_data', models.CharField(max_length=10)),
            ],
        ),
    ]