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
	course 		= Course.objects.all()
	params 		= {'course': course}

	if request.user.is_authenticated:
	    profile 	= Profile.objects.filter(user=request.user).first()
	    request.session['profile'] = profile.is_pro

	return render(request, "index.html", params)

def register(request):
    if request.method == "POST":
        username 		= request.POST.get('username')
        email 			= request.POST.get('email')
        password 		= request.POST.get('password')
        
        user = User.objects.filter(username=username)
        
        if user:
            messages.error(request, 'User already exists')
        else :
            user = User(username = username, email=email)
            user.set_password(password)
            user.save()

            Profile.objects.create(user=user)
            messages.success(request, 'User created successfully')
        
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

@login_required(login_url='/login/')
def view_course(request,slug):
    course 				= Course.objects.filter(slug =slug).first()
    course_modules 		= CourseModule.objects.filter(course=course)
    
    params = {'course':course , 'course_modules':course_modules}
    return render(request, 'course.html' , params)

@login_required(login_url='/login/')
def become_pro(request):
    if request.method == 'POST':
        membership = request.POST.get('membership' , 'MONTHLY')
        amount = 1000
        if membership == 'YEARLY':
            amount = 11000
        stripe.api_key = 'sk_test_qu7ivgHp9WRHlHJjs2QHugIA00hKFbC5qc'

        customer = stripe.Customer.create(
            email = "abhijeetg40@gmail.com",
            name=request.user.username,
            source=request.POST['stripeToken']
            )
            
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='inr',
            description="Membership",   
        )
        
        print(charge['amount'])
        if charge['paid'] == True:
            profile = Profile.objects.filter(user = request.user).first()
            if charge['amount'] == 100000:
                profile.subscription_type = 'M'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(30)
                profile.pro_expiry_date = expiry
                profile.save()
                
            elif charge['amount'] == 1100000:
                profile.subscription_type = 'Y'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(365)
                profile.pro_expiry_date = expiry
                profile.save()
        
        print(charge)
        return redirect('/charge/')
   
    return render(request, 'become_pro.html')

def charge(request):
    return render(request, 'charge.html')