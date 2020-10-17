from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=50)
	emailid = models.EmailField(max_length=50)
	city = models.CharField(max_length=100,blank=True,null=True)
	marks = models.IntegerField(default=0,blank=True,null=True)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Blog(models.Model):
	user1 = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
	author = models.CharField(max_length=20)
	comment = models.TextField(max_length=200)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.comment