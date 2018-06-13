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
        import argparse
        from django.db.models import Count,Sum
        from report.models import HitReport
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
print qs



'''
if args.format and args.logfile:
    logFormat = LogFormat.objects.all()
    logFormat = LogFormat.objects.get(name=args.format)
    load = process_import(args,logFormat)
'''        
    