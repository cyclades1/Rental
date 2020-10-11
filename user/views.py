from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Room , House
from django.template import loader


def profile(request):
	emil = request.session['member_id']
	user = User.objects.filter(email= email)
	template = loader.get_template('user/index.html')
	context = {
		'user':user,
	}
	return render(request, 'user/profile.html')

def post(request):
	user = request.session['member_id']
	return render(request, 'user/post.html', {'user':user})
