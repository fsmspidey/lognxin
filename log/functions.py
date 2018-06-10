import re
from log.models import LogFormat, LogField
from data.models import Load, Data
from django.utils import timezone
from datetime import *
import pytz

def process_line(line, logFormat, load):

    def process_field(log_field):        
    
        value = fields[log_field.position]

        if log_field.field.type == 2:
            value = datetime.strptime(fields[log_field.position], logFormat.date_format) 
            tz = pytz.timezone('UTC')
            value = tz.localize(value, is_dst=True)
            #print value
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
