from django.shortcuts import render

from django.shortcuts import render

def home(request):
	context = {}
	template = "home.html"
	return render(request, template, context)