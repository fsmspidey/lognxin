# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from report.models import HitSizeReport, StatusCodeReport


admin.site.register(HitSizeReport)
admin.site.register(StatusCodeReport)