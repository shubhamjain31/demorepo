from django.db import models

# Create your models here.

class Payment(models.Model):
	user  	= models.CharField(max_length=100)
	amount  = models.IntegerField(default=0)

	def __str_(self) -> str:
		return self.user
