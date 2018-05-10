from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	# return HttpResponse('aboutus')
	return render(request, 'home/index.html')

def aboutus(request):
	# return HttpResponse('aboutus')
	return render(request, 'home/aboutus.html')

def cancer(request):
	# return HttpResponse('aboutus')
	return render(request, 'cancer/cancer.html')

def visualization(request):
	# return HttpResponse('aboutus')
	return render(request, 'visualization/visualization.html')

def tweet(request):
	# return HttpResponse('aboutus')
	return render(request, 'tweet/tweet.html')