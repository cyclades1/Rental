from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=25)
	email = models.CharField(max_length = 100,primary_key=True)
	password = models.CharField(max_length=100)
	location = models.CharField(max_length=50)
	number = models.IntegerField()
	def __str__(self):
		return self.name 
		
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(user=instance)
#     instance.profile.save()

class Room(models.Model):
	room_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=25)
	user_email = models.CharField(max_length = 100)
	dimention = models.CharField(max_length=100)
	location = models.CharField(max_length=50)
	cost = models.IntegerField()
	kitchen = models.CharField(max_length=3)
	

class House(models.Model):
	house_id = models.AutoField(primary_key=True)
	user_email = models.CharField(max_length = 100)
	dimention = models.IntegerField()
	location = models.CharField(max_length=50)
	cost = models.IntegerField()
	floors = models.IntegerField()
	bedrooms= models.IntegerField()
	kitchen =models.IntegerField()
	hall = models.CharField(max_length=3)
	balcany = models.CharField(max_length=3)
	comment = models.CharField(max_length=200)
	