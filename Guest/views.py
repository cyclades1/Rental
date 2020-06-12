from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from django.template import loader
from user.models import *
from datetime import *



def index(request):
    return render(request, 'index.html')

def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def registerpage(request):
	return render(request, 'register.html',{'msg':""})

def loginpage(request):
	return render(request, 'login.html', {'msg':""})

def register(request):
	name = request.POST['name']
	email = request.POST['email']
	location = request.POST['location']
	phone = request.POST['phone']
	try:
		phone = int(phone)
	except:
		template = loader.get_template('register.html')
		context={
			'msg':'expection number in phone number'
		}
		return HttpResponse(template.render(context, request))
	pas = request.POST['pass']
	already = User.objects.filter(email= email)
	if bool(already):
		template = loader.get_template('register.html')
		context={
			'msg':"email already registered"
		}
		return HttpResponse(template.render(context, request))
	user = User(name = name , email = email , location= location, number = phone, password = pas)
	user.save()
	request.session['member_id']=email
	template = loader.get_template('profile.html')
	context = {
		'user':user,
	}
	return HttpResponse(template.render(context, request))

def login(request):
	email = request.POST['email']
	pas = request.POST['pass']
	user = User.objects.filter(email= email, password= pas)
	if bool(user):
			request.session['member_id']=email
			# template = loader.get_template('profile.html')
			# context={
			# 'user':user
			# }
			# return HttpResponse(template.render(context, request))
			return profile(request)
	else:
		template = loader.get_template('login.html')
		context={
		'msg':"wrong email or password"
		}
		return HttpResponse(template.render(context, request))


def profile(request):
	email = request.session['member_id']
	user = User.objects.get(email= email)
	if bool(user) and user!="":
		template = loader.get_template('profile.html')
		context = {
			'user':user,
		}
		return HttpResponse(template.render(context,request))
	else:
		del request.session['member_id']
		return render(request, 'index.html')

def post(request):
	email = request.session['member_id']
	user = User.objects.get(email= email)
	if bool(user) and user!="":
		template = loader.get_template('post.html')
		context = {
			'user':user,
		}
		return HttpResponse(template.render(context, request))
	else:
		del request.session['member_id']
		return render(request, 'index.html')

def logout(request):
	try:
		del request.session['member_id']
	except KeyError:
		pass
	return render(request, 'index.html')

