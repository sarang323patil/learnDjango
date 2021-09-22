# I have made this File
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	
	return render(request, 'index.html')
	#return HttpResponse('''<h1>HOME</h1> <a href="https://www.google.co.in/"> My Link </a>''')


def analyze(request):
	# get the text
	djtext = request.POST.get('text', 'default')
	removepunc = request.POST.get('removepunc', 'default')
	fulcaps = request.POST.get('fulcaps', 'default')
	# Analyze the text
	analyzed = ""
	punctuation = ''':;()[]}{<>!@?/|-_=+-*%^.'",&'''
	for char in djtext:
		if(char not in punctuation):
			analyzed += char 
	print(djtext, removepunc, fulcaps)
	
	if(removepunc != "on"):
		analyzed = djtext
	if(fulcaps == "on"):
		print("capitalize")
		analyzed = analyzed.upper() 

	params = {'purpose':'Remove Puctuation', 'analyzed':analyzed}
	return render(request, 'analyze.html', params)
