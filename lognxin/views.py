#https://docs.djangoproject.com/en/1.7/topics/templates/
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.models import Site
from log.models import LogFormat

def index(request):
	sites = Site.objects.all()
	formats = LogFormat.objects.all()
	
	return render(request, 'home/index.html', {'site_list': sites,'format_list': formats})

def report(request,site,format):
	print site
	return render(request, 'report/index.html')
