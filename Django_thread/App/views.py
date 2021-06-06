from django.shortcuts import render
from .models import *

from faker import Faker
fake = Faker()

from .thread import *
import random, time

# Create your views here.

def home(request):
	return render(request , 'index.html' )

async def datasend(request):
	for i in range(1, 10):
		channel_layer = get_channel_layer()
		data = {'count':i}
		await(channel_layer.group_send)(
            'new_consumer_group', {
            'type':'send_notification',
            'value':json.dumps(data)
            })
		time.sleep(1)
	return render(request , 'index.html' )	