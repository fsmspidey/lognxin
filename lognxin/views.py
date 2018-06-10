from django.http import HttpResponse
from django.shortcuts import render

def current_datetime(request):
	return render(request, 'home/index.html')