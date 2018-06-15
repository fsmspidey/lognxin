#https://docs.djangoproject.com/en/1.7/topics/templates/
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.models import Site
from log.models import LogFormat
from report.models import HitSizeReport
from django.db.models import Count,Sum

def index(request):
	sites = Site.objects.all()
	formats = LogFormat.objects.all()
	
	return render(request, 'home/index.html', {'site_list': sites,'format_list': formats})

def report(request,site,format):
	print site

 	#Data.objects.filter(load__pk=22).extra( select={"d": 'strftime("%%Y-%%m-%%d %%H",data_data.date_field)'} ).values('d').annotate(Count('load'), Sum('size_field'))

	site = Site.objects.get(domain=site)
	hit_size_report = HitSizeReport.objects.filter(load__site=site)\
						.extra( select={"d": 'strftime("%%Y-%%m-%%d",report_hitsizereport.date_time)'} ).values('d')\
						.annotate(hits=Sum('count'), traffic=Sum('size')/1024).order_by('-d')[:50]
	#print hit_size_report.query
	#print hit_size_report
	return render(request, 'report/index.html', { 'hit_size_report_list': hit_size_report })
