from django.db import models
from django.db.models import signals

def create_customer(sender, instance, created, **kwargs):
    print("Save is called")

class Customer(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=32)

    def __str__(self):
    	return self.name	

signals.post_save.connect(receiver=create_customer, sender=Customer)