from django.http import HttpResponse
from django.shortcuts import render
<<<<<<< Updated upstream

def current_datetime(request):
	return render(request, 'home/index.html')
=======
from data.models import Load
from django.contrib.sites.models import Site

def index(request):
	sites = Site.objects.all()
	return render(request, 'home/index.html', {'sites': sites})
>>>>>>> Stashed changes
