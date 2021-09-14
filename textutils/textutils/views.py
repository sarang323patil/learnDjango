# I have made this File
from django.http import HttpResponse

def index(request):
	return HttpResponse('''<h1>hello</h1> <a href="https://www.google.co.in/"> My Link </a>''')

def about(request):
	return HttpResponse("about sarang")