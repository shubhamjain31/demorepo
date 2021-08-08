from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User

from .models import *

# Create your views here.


def index(request):
	return HttpResponse('Done')

def add_student(request):
	student = Student.objects.create(first_name="Sarthak", 
									last_name="Jain", 
									age=24, 
									email="sarthak31@gmail.com", 
									mobile="8863638291", 
									website="http://www.sarthakcool.com/",
									section="B")
	return HttpResponse('<h1>Student Added</h1>')

def add_teacher(request):
	user = User.objects.last()

	teacher = Teacher.objects.create(name="Suniel Singh",
									user=user)
	return HttpResponse('<h1>Teacher Added</h1>')

def add_classroom(request):
	# classroom = Classroom.objects.create(student="Suniel Singh",
	# 									teacher=)
	return HttpResponse('<h1>Classroom Added</h1>')

def add_courses(request):
	return HttpResponse('Done')

def add_grade(request):
	return HttpResponse('Done')