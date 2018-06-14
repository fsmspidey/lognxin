# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from report.models import HitSizeReport


admin.site.register(HitSizeReport)