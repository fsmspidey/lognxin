# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.sites.models import Site
from log.models import LogFormat, Field

# Create your models here.
class Load(models.Model):
	log = models.CharField(max_length=250)
	import_date = models.DateTimeField(default=datetime.datetime.now)
	import_date_finish = models.DateTimeField(null=True)
	log_format = models.ForeignKey(LogFormat, on_delete=models.CASCADE, default='([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.*?) "(.*?)" "(.*?)"')
	tag = models.CharField(max_length=250, null=True, blank=True)
	site = models.ForeignKey(Site, on_delete=models.CASCADE)
	def __str__(self):
		return self.log

class Data(models.Model):
	load = models.ForeignKey(Load, on_delete=models.CASCADE)
	host_field = models.CharField(max_length=255, null=True)
	status_field = models.PositiveIntegerField(null=True)
	size_field = models.PositiveIntegerField(null=True)
	date_field = models.DateTimeField(null=True)
	url_field = models.CharField(max_length=255, null=True)
	url_field_method = models.CharField(max_length=10, null=True)
	url_field_uri = models.CharField(max_length=255, null=True)
	url_field_protocol = models.CharField(max_length=50, null=True)


