from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.models import Site

def index(request):
	sites = Site.objects.all()
	return render(request, 'home/index.html', {'site_list': sites})
