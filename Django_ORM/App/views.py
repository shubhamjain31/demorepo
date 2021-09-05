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
	students	 = Student.objects.all()
	teachers	 = Teacher.objects.all()

	classroom = Classroom.objects.create(student=students[2],
										teacher=teachers[1])
	return HttpResponse('<h1>Classroom Added</h1>')

def add_courses(request):
	students	 = Student.objects.all()

	course = Courses.objects.create(course_code="Course-CS",
									course_name="BCA",
									duration="1")

	course.students.add(students[1],students[0],students[2])
	return HttpResponse('<h1>Course Added</h1>')

def add_grade(request):
	students	 = Student.objects.all()

	grade = Grade.objects.create(student=students[0],
								 course="BCS",
								 grade=3)
	return HttpResponse('<h1>Grade Added</h1>')

def edit_student(request, id):
	student = Student.objects.get(pk=id)

	student.first_name 	= 'Abhay'
	student.last_name 	= 'Sharma'
	student.age 		= '28'
	student.email 		= 'abhay61@gmail.com'
	student.mobile 		= '9238238291'
	student.website 	= 'http://www.hero.com/'
	student.section 	= 'A'

	student.save()
	return HttpResponse('<h1>Student Updated</h1>')

def edit_teacher(request, id):
	user = User.objects.get(username="ram01")

	teacher = Teacher.objects.get(pk=id)

	teacher.name = "Manoj Rai"
	teacher.user = user

	teacher.save()

	return HttpResponse('<h1>Teacher Updated</h1>')

def edit_classroom(request, id):
	students	 = Student.objects.all()
	teachers	 = Teacher.objects.all()

	classroom = Classroom.objects.get(pk=id)

	classroom.student = students[2]
	classroom.teacher = teachers[1]

	classroom.save()
	return HttpResponse('<h1>Classroom Updated</h1>')

def edit_courses(request, val):
	students	 = Student.objects.all()

	course = Courses.objects.get(pk=val)

	# course.course_code 	= "Course-LAW"
	course.course 		= "Law"
	course.duration 	= "5"
	# course.students.add()

	course.save()
	return HttpResponse('<h1>Course Updated</h1>')