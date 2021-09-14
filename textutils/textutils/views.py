# I have made this File
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	
	return render(request, 'index.html')
	#return HttpResponse('''<h1>HOME</h1> <a href="https://www.google.co.in/"> My Link </a>''')


def analyze(request):
	# get the text
	djtext = request.GET.get('text', 'default')
	removepunc = request.GET.get('removepunc', 'default')
	
	# Analyze the text
	analyzed = ""
	punctuation = ''':;()[]}{<>!@?/|-_=+-*%^.'",&'''
	for char in djtext:
		if(char not in punctuation):
			analyzed += char 
	print(djtext, removepunc, analyzed)
	params = {'purpose':'Remove Puctuation', 'analyzed':analyzed}
	if(removepunc != "on"):
		analyzed = djtext
	return render(request, 'analyze.html', params)
'''
def removepunc(request):
	# get the text
	djtext = request.GET.get('text', 'default')

	# Analyze the text
	return HttpResponse(''remove punc <a href="/">back</a>')


def capfirst(request):
	return HttpResponse("capitalize first")

def newlinerem(request):
	return HttpResponse("new line remove")

def spacerem(request):
	return HttpResponse("space remove")

def charcount(request):
	return HttpResponse("char count")

'''