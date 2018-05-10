from django.shortcuts import render
from django.http import HttpResponse

def aboutus(request):
	# return HttpResponse('aboutus')
	return render(request, 'home/aboutus.html')

