# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Load, Data

class LoadAdmin(admin.ModelAdmin):
    #model = Load
    ordering = ['-import_date']
    list_display = ('log','log_format','site','import_date','import_date_finish')

admin.site.register(Load, LoadAdmin)
admin.site.register(Data)