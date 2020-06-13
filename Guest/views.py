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
import re



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
	city = request.POST['city']
	state = request.POST['state']
	phone = request.POST['phone']
	pas = request.POST['pass']
	cpas = request.POST['cpass']
	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	if(re.search(regex,email)):
		pass
	else:
		template = loader.get_template('register.html')
		context={
			'msg':'invalid email'
		}
		return HttpResponse(template.render(context, request))

	if len(str(phone)) !=  10:
		template = loader.get_template('register.html')
		context={
			'msg':'invalid phone number'
		}
		return HttpResponse(template.render(context, request))
	
	if pas != cpas:
		template = loader.get_template('register.html')
		context={
			'msg':'password did not matched'
		}
		return HttpResponse(template.render(context, request))
	already = User.objects.filter(email= email)
	if bool(already):
		template = loader.get_template('register.html')
		context={
			'msg':"email already registered"
		}
		return HttpResponse(template.render(context, request))
	user = User(name = name , email = email , location= location,city= city, state = state, number = phone, password = pas)
	user.save()
	request.session['member_id']=email
	template = loader.get_template('profile.html')
	return profile(request)

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
		room= Room.objects.filter(user_email= user)
		if bool(room):
			context.update({'room':room})
		house = House.objects.filter(user_email= user)
		if bool(house):
			context.update({'house':house})
		
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



def posth(request):
	email = request.session['member_id']
	user = User.objects.get(email= email)
	if bool(user) and user!="":
		template = loader.get_template('posth.html')
		context = {
			'user':user,
		}
		return HttpResponse(template.render(context, request))
	else:
		del request.session['member_id']
		return render(request, 'index.html')


def postedh(request):
	email = request.session['member_id']
	user = User.objects.get(email= email)
	if bool(user) and user!="":
		area = request.POST['area']
		floor = request.POST['floor']
		location = request.POST['location']
		city = request.POST['city']
		state = request.POST['state']
		cost = request.POST['cost']
		hall = request.POST['hall']
		kitchen = request.POST['kitchen']
		balcany = request.POST['balcany']
		bedroom = request.POST['bedroom']
		ac = request.POST['AC']
		desc = request.POST['desc']
		img = request.FILES['img']
		house = House(user_email = user, location=location, city=city, state=state, cost = cost, hall=hall, 
			kitchen=kitchen, balcany=balcany, bedrooms=bedroom,area=area, floor=floor, AC = ac, desc= desc, img=img)
		house.save()
		return render(request, 'post.html', {'msg':'submitted successfully..'})

	else:
		del request.session['member_id']
		return render(request, 'index.html')


def postedr(request):
	email = request.session['member_id']
	user = User.objects.get(email= email)
	if bool(user) and user!="":
		dimention = request.POST['dimention']
		location = request.POST['location']
		city = request.POST['city']
		state = request.POST['state']
		cost = request.POST['cost']
		hall = request.POST['hall']
		kitchen = request.POST['kitchen']
		balcany = request.POST['balcany']
		bedroom = request.POST['bedroom']
		ac = request.POST['AC']
		desc = request.POST['desc']
		img = request.FILES['img']
		room = Room(user_email = user, dimention=dimention, location=location, city=city, state=state, cost = cost, hall=hall, 
			kitchen=kitchen, balcany=balcany, bedrooms=bedroom, AC = ac, desc= desc, img=img)
		room.save()
		return render(request, 'post.html', {'msg':'submitted successfully..'})

	else:
		del request.session['member_id']
		return render(request, 'index.html')

def logout(request):
	try:
		del request.session['member_id']
	except KeyError:
		pass
	return render(request, 'index.html')

