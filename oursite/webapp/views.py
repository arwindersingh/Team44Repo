from django.shortcuts import render
from django.http import HttpResponse

def index (request):
	return render(request, 'webapp/home.html')
	# return HttpResponse("<h2>HEY!</h2>")

def map(request):
	return render(request, 'webapp/map.html')