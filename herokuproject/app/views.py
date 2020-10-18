from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from app.forms import LoginForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
	return render(request, 'index.html')

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
			print(password,confirmpassword)
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