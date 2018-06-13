import re
from log.models import LogFormat, LogField
from data.models import Load, Data
from django.utils import timezone
from datetime import datetime
from django.conf import settings
from django.contrib.sites.models import Site
from log.models import LogFormat
import pytz

def process_line(line, logFormat, load):

    def process_field(log_field):        
    
        def update_data(data):
            if "date" in (log_field.field.name).lower():
                data.date_field=value

            if "host" in (log_field.field.name).lower():
                data.host_field=value

            if "status" in (log_field.field.name).lower():
                data.status_field=value

            if "size" in (log_field.field.name).lower():
                try:
                    data.size_field=int(value)
                except:
                    data.size_field=0

            if "url" in (log_field.field.name).lower():
                data.url_field=value
                data.url_field_method=value.split(' ')[0]
                data.url_field_uri=value.split(' ')[1]
                data.url_field_protocol=value.split(' ')[2]                
            return data

        value = fields[log_field.position]
        if log_field.field.type == 2:
            value = datetime.strptime(fields[log_field.position], logFormat.date_format) 
            tz = pytz.timezone(settings.TIME_ZONE)
            value = tz.localize(value, is_dst=True)
        update_data(data)


    fields  = re.match( logFormat.regex, line).groups()
    log_fields = LogField.objects.filter(log_format=logFormat.pk).order_by("position")
    
    data = Data(load=load)    
    for log_field in log_fields:
        process_field(log_field)
    data.save()

def process_import(args,logFormat):
    print "Importing - Format: "+ logFormat.name
    with open(args.logfile) as f:
            lines = f.readlines()

    now = datetime.now()
    tz = pytz.timezone(settings.TIME_ZONE)
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
            print str(round(float(line_completed*100)/total_lines,2)) + "% completed"

    now = datetime.now()
    tz = pytz.timezone(settings.TIME_ZONE)
    now = tz.localize(now, is_dst=True)
    load.import_date_finish = now
    load.save(update_fields=['import_date_finish'])

    if load.pk>0 and line_completed>0:
        return load
    return False