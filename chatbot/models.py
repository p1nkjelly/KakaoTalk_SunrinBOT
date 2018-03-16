# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class parsedmenu(models.Model):
	day = models.CharField(max_length=15)
	menu = models.CharField(max_length=35)

# Create your models here.
