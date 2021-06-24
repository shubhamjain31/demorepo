from django.shortcuts import render
# from django.contrib.auth.models import User
from .models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login

import sys
from django.core.management import BaseCommand, call_command

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

from ipware import get_client_ip
from faker import Faker
from .models import *

fake = Faker()

# Create your views here.

# ********************************************************** For Management Command *************************************************************

def index(request):

	user = authenticate(email="sj27754@gmail.com", password="shubham")
	# login(request, user)
	print(request.user)
	# sysout = sys.stdout
	# sys.stdout = open('filename.json', 'w')
	# call_command('initdata')
	# sys.stdout = sysout
	return HttpResponse('Done')

# ********************************************************** For Autocomplete Search Bar *************************************************************

def generate_data(request):

	# generate fake addresses
	for i in range(0, 100):
		FakeAddress.objects.create(address = fake.address())
	return JsonResponse({'status':200})

def home(request):
	return render(request, "index.html")


#search/?address=val
def search_address(request):
	address = request.GET.get("address")

	payload = []
	if address:
		fake_address_obj = FakeAddress.objects.filter(address__icontains = address)

		for obj in fake_address_obj:
			payload.append(obj.address)
	return JsonResponse({'status':200, 'data':payload})