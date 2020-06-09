from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from django.template import loader
from user.models import User



def index(request):
    return render(request, 'index.html')

def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def register(request):
	return render(request, 'register.html')

def add(request):
	name = request.POST['name']
	email = request.POST['email']
	location = request.POST['location']
	phone = request.POST['phone']
	pas = request.POST['pass']
	user = User(name = name , email = email , location= location, number = phone, password = pas)
	user.save()
	template = loader.get_template('user/profile.html')
	context = {
		'user':user,
	}
	return HttpResponse(template.render(context, request))

def login(request):
	email = request.POST['email']
	pas = request.POST['pass']
	user = User.objects.filter(email= email, password= pas)
	# return render(request, 'user/index.html', {'users': user})
	if bool(user):
			template = loader.get_template('user/profile.html')
			context={
			'user':user
			}
			return HttpResponse(template.render(context, request))
	else:
		return HttpResponse("wrong email or password")
