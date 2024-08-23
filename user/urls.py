from django.urls import path, re_path
from django.contrib.auth import logout
from . import views

urlpatterns =[
	re_path(r'profile', views.profile, name= 'profile'),
	re_path(r'post',views.post, name = 'post'),
]
