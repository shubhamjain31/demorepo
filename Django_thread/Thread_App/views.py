from django.shortcuts import render
from .models import *

from faker import Faker
fake = Faker()
import random

from .thread import CreateStudentThread

# Create your views here.

def mythread(request):
	count = 100

	# without threading
	# for i in range(count):
	# 	print(i)
	# 	Student_Data.objects.create(
	# 		student_name 		= fake.name(),
	# 	    student_email 		= fake.email(),
	# 	    address 			= fake.address(),
	# 	    age 				= random.randint(15, 50)
	# 		)

	# with threading
	CreateStudentThread(count).start()

	return render(request , 'mythread.html' )