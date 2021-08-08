from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.


def index(request):
	return HttpResponse('Done')

def add_student(request):
	student = Student.objects.create(first_name="Shubham", last_name="Jain", age=26, email="shubhamjain@gmail.com", 
				mobile="9876543312", website="http://www.mywebsite.com/", section="Alpha")
	return HttpResponse('Done')

def add_teacher(request):
	return HttpResponse('Done')

def add_classroom(request):
	return HttpResponse('Done')

def add_courses(request):
	return HttpResponse('Done')

def add_grade(request):
	return HttpResponse('Done')