from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import *
from App.forms import StudentForm, UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

# Create your views here.

def home(request):
	obj = Student.objects.all().order_by('-date')
	params = {"obj":obj}
	return render(request, "index.html", params)

def studentform(request):
	obj = Student.objects.all().order_by('-date')
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/studentform/')
	else:
		form = StudentForm()
		params = {"form":form, "data":obj}
	return render(request, 'student.html', params)

def register(request):
	if request.method == "POST":
		new_form = UserForm(request.POST)
		if new_form.is_valid():
			username = new_form.cleaned_data['username']
			firstname = new_form.cleaned_data['first_name']
			lastname = new_form.cleaned_data['last_name']
			email = new_form.cleaned_data['email']
			password = new_form.cleaned_data['password']
			confirmpassword = new_form.cleaned_data['confirm_password']
			if password == confirmpassword:
				User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
				messages.success(request, "User Registration Successfully !!")
				usr = auth.authenticate(username=username,password=password)
				auth.login(request,usr)
				return render(request, 'welcome.html')
			else:
				messages.error(request, "Password and Confirm Password does not match !!")
				return HttpResponseRedirect('/register/')
	else:
		new_form = UserForm()
	return render(request, 'register.html', {"new_form":new_form})

#1st Way for login
'''def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request, user)
				return render(request, 'welcome.html')
			else:
				messages.error(request, "Username and Password did not matched !!")
		except auth.ObjectDoesNotExist:
			print("Invalid User")
	return render(request, 'login.html')'''

#2nd Way for login
def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request, user)
				return render(request, 'welcome.html')
			else:
				messages.error(request, "Username and Password did not matched !!")
		except auth.ObjectDoesNotExist:
			print("Invalid User")
	else:
		form = LoginForm()
	return render(request, 'login.html', {"form":form})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login')

def search(request):
	if request.method == "POST":
		search = request.POST['search']
		if search:
			match = Student.objects.filter(Q(name__icontains=search)|Q(city__icontains=search))
			
			if match:
				return render(request, 'search.html', {'data':match})
			else:
				messages.error(request, "No result found")
		else:
			return HttpResponseRedirect('/search/')
	return render(request, 'search.html')