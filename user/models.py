from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=25)
	email = models.CharField(max_length = 100,primary_key=True)
	password = models.CharField(max_length=100)
	birth_date = models.DateField()
	number = models.IntegerField()
	def __str__(self):
		return self.name 
		