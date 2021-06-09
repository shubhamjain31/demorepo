from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name 			= models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Post(models.Model):
	category 		= models.ForeignKey(Category, on_delete = models.PROTECT, default=1)
	title 			= models.CharField(max_length = 200)
	excerpt 		= models.TextField(null = False)
	content 		= models.TextField()
	author 			= models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_name')

	def __str__(self):
		return self.title		