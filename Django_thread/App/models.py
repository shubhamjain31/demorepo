from django.db import models
from django.contrib.auth.models import User

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your models here.

class Informations(models.Model):
    text 				= models.CharField(max_length=100)
    json_data 			= models.TextField(default="{}")

class Images(models.Model):
    image 				= models.ImageField(upload_to='images')

class Students(models.Model):
    student_name 		= models.CharField(max_length=100)
    student_email 		= models.EmailField(max_length=100)
    address 			= models.CharField(max_length=100)
    age 				= models.IntegerField()
    
    def __str__(self):
        return self.student_name

class Notifications(models.Model):
    user 				= models.ForeignKey(User, on_delete=models.CASCADE)
    notifications 		= models.TextField(max_length=100)
    is_seen 			= models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)


    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        
        notification_obj = Notifications.objects.filter(is_seen=False).count()
        data = {'count':notification_obj, 'current_notification':self.notifications}
        
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group', {
            'type':'send_notification',
            'value':json.dumps(data)
            })
        super(Notifications, self).save(*args, **kwargs)