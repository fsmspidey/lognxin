# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LogFormat(models.Model):
	name = models.CharField(max_length=150)
	date_format = models.CharField(max_length=200, default='%d/%b/%Y:%H:%M:%S -0300')
	regex = models.CharField(max_length=250, default='([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"')
	def __str__(self):
		return self.name

class Field(models.Model):
	TYPES = (
	    (0, 'Char'),
	    (1, 'Int'),
	    (2, 'DateTime'),
	)
	name = models.CharField(max_length=150)
	type = models.PositiveIntegerField(
										choices=TYPES,
        								default=0
        								) 
	def __str__(self):
		return self.name

class LogField(models.Model):
	log_format = models.ForeignKey(LogFormat, on_delete=models.CASCADE, related_name="logformat")
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	position = models.PositiveIntegerField()
	

