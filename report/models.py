# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from data.models import Load

class HitSizeReport(models.Model):
	load 		= models.ForeignKey(Load, on_delete=models.CASCADE)
	date_time 	= models.DateTimeField()
	count		= models.PositiveIntegerField()
	size		= models.PositiveIntegerField()

