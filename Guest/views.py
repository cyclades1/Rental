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
import os

def no(request):
	return render(request, 'front.html')

def index(request):
	template = loader.get_template('index.html')
	try:
		email = request.session['member_id']
	except:
		email =""
	if bool(email):
		context={'base':'base.html',}
	else:
		context={'base':'Gbase.html',}
	
	room= Room.objects.all()
	if bool(room):
		n = len(room)
		nslide = n//3+ (n%3 >0)
		rooms = [room, range(1, nslide), n]
		context.update({'room':rooms})
	house = House.objects.all()
	if bool(house):
		n = len(house)
		nslide = n//3+ (n%3 >0)
		houses = [house, range(1, nslide), n]
		context.update({'house':houses})
	return HttpResponse(template.render(context,request))



def home(request):
	template = loader.get_template('home.html')
	try:
		email = request.session['member_id']
	except:
		email =""
	if bool(email):
		context={'base':'base.html',}
	else:
		context={'base':'Gbase.html',}
	context.update({'result':""})
	context.update({'msg':"Search your query"})
	return HttpResponse(template.render(context,request))

def  search(request):
	template = loader.get_template('home.html')
	try:
		email = request.session['member_id']
	except:
		email =""
	if bool(email):
		context={'base':'base.html',}
	else:
		context={'base':'Gbase.html',}
	if request.method == 'GET':
		typ = request.GET['type']
		if bool(typ):
		 	q = request.GET['q']
		 	if typ=="House" and ( bool( House.objects.filter(location=q)) or bool( House.objects.filter(city=q))):
		 		results= House.objects.filter(location=q)
		 		results= results | House.objects.filter(city=q)
		 	elif typ!="House" and ( bool( Room.objects.filter(location= q)) or bool( House.objects.filter(city=q))):
		 		results = Room.objects.filter(location= q)
		 		results= results | Room.objects.filter(city=q)
		 	else:
		 		context.update({'msg':'No result found for matching query'})
		 		return HttpResponse(template.render(context,request))
		 	result= [results, len(results)]
		 	context.update({'result':result})
		 	context.update({'type':typ})
		else:
			context.update({'msg':'Undefined search type'})
	
		
	return HttpResponse(template.render(context,request))

	

def about(request):
	template = loader.get_template('about.html')
	try:
		email = request.session['member_id']
	except:
		email =""
	if bool(email):
		context={'base':'base.html',}
	else:
		context={'base':'Gbase.html',}
	
	room= Room.objects.all()
	if bool(room):
		context.update({'room':room})
	house = House.objects.all()
	if bool(house):
		context.update({'house':house})
	return HttpResponse(template.render(context,request))

def contact(request):
	template = loader.get_template('contact.html')
	try:
		email = request.session['member_id']
	except:
		email =""
	if bool(email):
		context={'base':'base.html',}
	else:
		context={'base':'Gbase.html',}
	
	if request.method == 'POST':
		subject = request.POST['subject']
		email = request.POST['email']
		body = request.POST['body']
		regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
		if(re.search(regex,email)):
			pass
		else:
			template = loader.get_template('register.html')
			context.update({'msg':'invalid email'})
			return HttpResponse(template.render(context, request))
		contact = Contact(subject= subject, email= email, body = body)
		contact.save()
		context.update({'msg':'msg send to admin'})
		return HttpResponse(template.render(context,request))
	else:
		context.update({'msg':''})
		return HttpResponse(template.render(context,request))

def descr(request):
	template = loader.get_template('desc.html')
	try:
		email = request.session['member_id']
	except:
		email =""
	if bool(email):
		context={'base':'base.html',}
	else:
		context={'base':'Gbase.html',}
	if request.method == "GET":
		id = request.GET['id']
		try:
			room =Room.objects.get(room_id=id)
			context.update({'val':room})
			context.update({'type':'Apartment'})
			user = User.objects.get(email = room.user_email)
		except:
			house =House.objects.get(house_id=id)
			context.update({'val':house})
			context.update({'type':'House'})
			user = User.objects.get(email = house.user_email)
	context.update({'user':user})
	return HttpResponse(template.render(context,request))


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
		report = Contact.objects.filter(email= user.email)
		context.update({'reportno':len(report)})
		room= Room.objects.filter(user_email= user)
		if bool(room):
			context.update({'room':room})
		context.update({'roomno':len(room)})
		house = House.objects.filter(user_email= user)
		if bool(house):
			context.update({'house':house})
		context.update({'houseno':len(house)})
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
		location = request.POST['location'].lower()
		city = request.POST['city'].lower()
		state = request.POST['state'].lower()
		cost = request.POST['cost']
		hall = request.POST['hall'].lower()
		kitchen = request.POST['kitchen'].lower()
		balcany = request.POST['balcany'].lower()
		bedroom = request.POST['bedroom']
		ac = request.POST['AC'].lower()
		desc = request.POST['desc'].upper()
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
		location = request.POST['location'].lower()
		city = request.POST['city'].lower()
		state = request.POST['state'].lower()
		cost = request.POST['cost']
		hall = request.POST['hall'].lower()
		kitchen = request.POST['kitchen'].lower()
		balcany = request.POST['balcany'].lower()
		bedroom = request.POST['bedroom']
		ac = request.POST['AC'].lower()
		desc = request.POST['desc'].upper()
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
	return index(request)

def deleter(request):
	if request.method =="GET":
		id = request.GET['id']
		instance = Room.objects.get(room_id=id)
		instance.delete()
	return profile(request)


def deleteh(request):
	if request.method == "GET":
		id = request.GET['id']
		instance =House.objects.get(house_id=id)
		instance.delete()
	return profile(request)

