# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from data.models import Load

# Create your models here.
class HitReport(models.Model):
	load 		= models.ForeignKey(Load, on_delete=models.CASCADE)
	date_time 	= models.DateTimeField()
	count		= models.PositiveIntegerField()

