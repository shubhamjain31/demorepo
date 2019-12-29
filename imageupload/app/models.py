from django.db import models

# Create your models here.


class Login(models.Model):
	Username = models.CharField(max_length=50,default='')
	Password = models.CharField(max_length=50,default='')
	Usertype = models.CharField(max_length=50,default='')

	def __str__(self):
		return self.Username

class Pics(models.Model):
	pic_id = models.AutoField(primary_key=True)
	Picture = models.ImageField(upload_to='images')