from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns =[
	path('',views.index,name= 'index'),
	path('home/',views.home, name='home'),
	path('about/',views.about,name='about'),
	path('contact/',views.contact,name='contact')
]
