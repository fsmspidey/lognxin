#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lognxin.settings")
    try:
        import django
        django.setup()        
        from django.contrib.sites.models import Site
        from log.functions import *
        import argparse, re
    except ImportError:
        raise ImportError(
              "Couldn't import Models and Django. Are you sure it's installed and "
              "available on your PYTHONPATH environment variable? Did you "
              "forget to activate a virtual environment?"
        )

parser = argparse.ArgumentParser()
parser.add_argument("-l","--logfile", type=str)
parser.add_argument("-f","--format", type=str)
parser.add_argument("-t","--tag", type=str)
args = parser.parse_args()

if args.format:
    logFormat = LogFormat.objects.all()
    print logFormat
    logFormat = LogFormat.objects.get(name=args.format)
    print logFormat.name

    with open(args.logfile) as f:
        lines = f.readlines()

    now = datetime.now()
    tz = pytz.timezone('UTC')
    now = tz.localize(now, is_dst=True)

    site = Site.objects.get(domain='example.com')
    load = Load(log=args.logfile, log_format=logFormat, site=site, tag=args.tag, import_date=now)
    load.save()
    
    if load.pk>0:
        total_lines = len(lines)
        line_completed=0
        for line in lines:
            process_line(line.rstrip('\n'), logFormat, load)
            line_completed = line_completed + 1
            print str(float((line_completed*100)/total_lines)) + "% completed"

    now = datetime.now()
    tz = pytz.timezone('UTC')
    now = tz.localize(now, is_dst=True)
    load.import_date_finish = now
    load.save(update_fields=['import_date_finish'])