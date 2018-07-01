#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lognxin.settings")
    try:
        import django
        from django.conf import settings
        django.setup()        
        from log.functions import process_import
        from log.models import LogFormat
        from data.models import Load, Data
        from report.models import HitSizeReport, StatusCodeReport
        import argparse
        from django.db.models import Count,Sum
        
    except ImportError:
        raise ImportError(
              "Couldn't import Models and Django. Are you sure it's installed and "
              "available on your PYTHONPATH environment variable? Did you "
              "forget to activate a virtual environment?"
        )

parser = argparse.ArgumentParser()
parser.add_argument("-l",   "--logfile" , type=str)
parser.add_argument("-f",   "--format"  , type=str)
parser.add_argument("-t",   "--tag"     , type=str)
args = parser.parse_args()

#from django.db.models import Count
''' hits '''

print "hits & bytes"
qs = Data.objects.filter(load__pk=79).extra( select={"d": 'strftime("%%Y-%%m-%%d %%H",data_data.date_field)'} ).values('d').annotate(Count('load'), Sum('size_field'))

print "Status Code report"
qs2 = Data.objects.filter(load__pk=79).extra( select={"d": 'strftime("%%Y-%%m-%%d %%H",data_data.date_field)'} ).values('d','status_field').annotate(Count('load'))

load = Load.objects.get(pk=79)
for data in qs:
    #print data
    hit_size_report = HitSizeReport(load=load,date_time=data['d']+":00:00+0000",count=data['load__count'],size=data['size_field__sum'])
    #hit_size_report.save()

for data in qs2:
    print data
    status_code_report = StatusCodeReport(load=load,date_time=data['d']+":00:00+0000",count=data['load__count'],status_code=data['status_field'])
    #status_code_report.save()



'''
if args.format and args.logfile:
    logFormat = LogFormat.objects.all()
    logFormat = LogFormat.objects.get(name=args.format)
    load = process_import(args,logFormat)
'''        
    