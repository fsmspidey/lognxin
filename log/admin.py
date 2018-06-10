# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import LogFormat, Field, LogField



class LogFieldsInline(admin.TabularInline):
    model = LogField

class LogFormatAdmin(admin.ModelAdmin):
    inlines = [
        LogFieldsInline,
    ]

admin.site.register(LogFormat,LogFormatAdmin)
admin.site.register(Field)
