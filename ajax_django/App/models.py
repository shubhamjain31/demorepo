from django.db import models
from rest_framework import serializers

# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=100)
	prize = models.IntegerField()
	pages = models.IntegerField()

	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    prize = serializers.IntegerField()
    pages = serializers.IntegerField()
    id = serializers.IntegerField()