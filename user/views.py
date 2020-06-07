from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader

def index(request):
	user_list = User.objects.order_by('name')
	template = loader.get_template('user/index.html')
	context = {
		'user_list':user_list,
	}
	return HttpResponse(template.render(context, request))

def home(request):
	return render(request,'user/home.html')

def about(request):
	return render(request,'user/about.html')

def contact(request):
	return render(request,'user/contact.html')

# def hello(request):
# 	return render(request,"polls/hello.html",{})
