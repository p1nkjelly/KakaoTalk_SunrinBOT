# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class parsedmenu(models.Model):
    day = models.CharField(max_length=15)
    menu = models.CharField(max_length=35)

    def __str__(self):
        return self.day[:-3]

class timetable_mon(models.Model):
    c_name = models.CharField(max_length=10)
    t_table = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

class timetable_tue(models.Model):
    c_name = models.CharField(max_length=10)
    t_table = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

class timetable_wed(models.Model):
    c_name = models.CharField(max_length=10)
    t_table = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

class timetable_thu(models.Model):
    c_name = models.CharField(max_length=10)
    t_table = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

class timetable_fri(models.Model):
    c_name = models.CharField(max_length=10)
    t_table = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name
