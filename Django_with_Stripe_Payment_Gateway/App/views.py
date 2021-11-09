from django.shortcuts import render, redirect
from django.conf import settings
from django.db.models import Q

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import stripe
from datetime import datetime, timedelta

from .models import *

# Create your views here.

def index(request):
	params = {"key": settings.STRIPE_PUBLISHABLE_KEY}
	return render(request, "index.html", params)

def register(request):
    if request.method == "POST":
        username 		= request.POST.get('username')
        password 		= request.POST.get('password')
        
        user = User.objects.filter(username=username)
        
        if user:
            params = {'message' : 'User already exists' , 'class' : 'danger'}
        else :
            params = {'message' : 'User created successfully' , 'class' : 'success'}
            user = User(username = username)
            user.set_password(password)
            user.save()
        
    return render(request,'register.html')

def login_attempt(request):
    if request.method == "POST":
        username_or_email 		= request.POST.get('username_or_email')
        password 				= request.POST.get('password')
        
        user = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()
        
        if user is None:
            messages.error(request, 'No user found')
            return render(request,'login.html')
        else:
            user = authenticate(request, username_or_email = username_or_email , password = password)
            if user is None:
                messages.error(request, 'Invalid credentials')
                return render(request,'login.html')
            else:
                login(request , user)
                return redirect('index') 

    return render(request,'login.html')

def logout_attempt(request):
    request.session.profile = None
    logout(request)
    return redirect('/')