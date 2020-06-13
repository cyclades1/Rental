from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length = 100,primary_key=True)
	name = models.CharField(max_length=25)
	password = models.CharField(max_length=100)
	location = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	number = models.IntegerField()
	def __str__(self):
		return self.email 
		

class Room(models.Model):
	room_id = models.AutoField(primary_key=True)
	user_email = models.ForeignKey(User, to_field='email',on_delete=models.CASCADE )
	dimention = models.CharField(max_length=100)
	location = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	cost = models.IntegerField()
	bedrooms= models.IntegerField()
	kitchen =models.CharField(max_length=3)
	hall = models.CharField(max_length=3)
	balcany = models.CharField(max_length=3)
	desc = models.CharField(max_length=200)
	AC = models.CharField(max_length=3)
	img = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100)
	date = models.DateField(auto_now=True, auto_now_add=False) 
	def __str__(self):
		return str(self.room_id)

class House(models.Model):
	house_id = models.AutoField(primary_key=True)
	user_email = models.ForeignKey(User, to_field='email',on_delete=models.CASCADE)
	area = models.IntegerField()
	floor = models.IntegerField()
	location = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	cost = models.IntegerField()
	bedrooms= models.IntegerField()
	kitchen =models.IntegerField()
	hall = models.CharField(max_length=3)
	balcany = models.CharField(max_length=3)
	desc = models.CharField(max_length=200)
	AC = models.CharField(max_length=3)
	img = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)
	date = models.DateField(auto_now=True, auto_now_add=False) 
	def __str__(self):
		return str(self.house_id)
	