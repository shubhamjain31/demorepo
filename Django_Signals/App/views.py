from django.shortcuts import render
from django.http import HttpResponse
from App.models import *

# Create your views here.

def index(request):
	obj = Customer(name='test', description='test in detail')
	obj.save()
	return HttpResponse('<html>Done</html>')