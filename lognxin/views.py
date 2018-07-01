#https://docs.djangoproject.com/en/1.7/topics/templates/
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.models import Site
from log.models import LogFormat
from report.models import HitSizeReport, StatusCodeReport
from django.db.models import Count,Sum
from django.db.models import F

def index(request):
	sites = Site.objects.all()
	formats = LogFormat.objects.all()
	
	return render(request, 'home/index.html', {'site_list': sites,'format_list': formats})

def report(request,site,format):
	site = Site.objects.get(domain=site)
	hit_size_report = HitSizeReport.objects.filter(load__site=site)\
						.extra( select={"d": 'strftime("%%Y-%%m-%%d %%H",report_hitsizereport.date_time)'} ).values('d')\
						.annotate(hits=Sum('count'), traffic=Sum('size')/1024).order_by('-d')[:50]
	
	if len(hit_size_report) > 0:
		max_date 	= 	(hit_size_report[0]['d'])[:11]+'00:00+0000'
		min_date 	= 	(hit_size_report[len(hit_size_report)-1]['d'])[:11]+'00:00+0000'

	status_code_report = StatusCodeReport.objects.filter(load__site=site, date_time__lte=max_date,date_time__gte=min_date)\
						.values('status_code')\
						.order_by('status_code').annotate(hits=Sum('count'))

	return render(request, 'report/index.html', { 'hit_size_report_list': hit_size_report, 'status_code_report_list': status_code_report })
