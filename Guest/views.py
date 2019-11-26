from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def register(request):
	return render(request,'register.html')
