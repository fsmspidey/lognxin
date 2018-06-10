#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lognxin.settings")
    try:
        import django
        django.setup()        
        from log.models import LogFormat, LogField
        from django.contrib.sites.models import Site
        from data.models import Load, Data
        from django.utils import timezone
        from datetime import *
        #from pytz import timezone
        import pytz
        import argparse, re
    except ImportError:
        raise ImportError(
            "Couldn't import Models and Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )


USE_TZ = False 
parser = argparse.ArgumentParser()
parser.add_argument("-l","--logfile", type=str)
parser.add_argument("-f","--format", type=str)
parser.add_argument("-t","--tag", type=str)
args = parser.parse_args()


def process_line(line, logFormat):

    def process_field(log_field):        
    

    
        value = fields[log_field.position]

        if log_field.field.type == 2:
            value = datetime.strptime(fields[log_field.position], logFormat.date_format) 
            tz = pytz.timezone('UTC')
            value = tz.localize(value, is_dst=True)
            print value
            #exec("data."+(log_field.field.name).lower()+"_field"+"=value")

        if "date" in (log_field.field.name).lower():
            data.date_field=value

        if "host" in (log_field.field.name).lower():
            data.host_field=value

        if "status" in (log_field.field.name).lower():
            data.status_field=value

    
        if "url" in (log_field.field.name).lower():
            data.url_field=value
            data.url_field_method=value.split(' ')[0]
            data.url_field_uri=value.split(' ')[1]
            data.url_field_protocol=value.split(' ')[2]


            
            #print datetime.strptime(fields[log_field.position], logFormat.date_format)
    #([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"
    fields  = re.match(
                    logFormat.regex, line
                    ).groups()

    log_fields = LogField.objects.filter(
                                            log_format=logFormat.pk)\
                                            .order_by("position"
                                        )
    data = Data(load=load)

    for log_field in log_fields:
        process_field(log_field)
    data.save()

if args.format:
    logFormat = LogFormat.objects.all()
    print logFormat
    logFormat = LogFormat.objects.get(name=args.format)
    print logFormat.name

if args.logfile:

    with open(args.logfile) as f:
        lines = f.readlines()

    site = Site.objects.get(domain='example.com')
    load = Load(log=args.logfile, log_format=logFormat, site=site)
    load.save()
    
    if load.pk>0:
        for line in lines:
            process_line(line.rstrip('\n'), logFormat)
    load.import_date_finish = datetime.now()
    load.save(update_fields=['import_date_finish'])