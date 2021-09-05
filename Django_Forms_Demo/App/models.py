from django.db import models

# Create your models here.

class Employee(models.Model):  
    name 				= models.CharField(max_length=100)  
    email  				= models.EmailField()  
    contact 			= models.CharField(max_length=15)
    date_created 		= models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:  
        db_table = "employee"

    def __str__(self):
    	return self.name