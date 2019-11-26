from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'user/index.html')

def home(request):
	return render(request,'user/home.html')

def about(request):
	return render(request,'user/about.html')

def contact(request):
	return render(request,'user/contact.html')

# def hello(request):
# 	return render(request,"polls/hello.html",{})
