# SHOP VIEWs

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'shop/index.html')

def about(request):
	return render(request, 'shop/about.html')

def contact(request):
	return HttpResponse("CONTACT")

def tracker(request):
	return HttpResponse("TRACKER")

def search(request):
	return HttpResponse("SEARCH")

def productView(request):
	return HttpResponse("PRODUCT VIEW")

def checkout(request):
	return HttpResponse("CHECKOUT")

