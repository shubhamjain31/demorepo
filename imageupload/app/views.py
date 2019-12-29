from django.shortcuts import render
from django.http import HttpResponse
from .models import Login,Pics
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect

# Create your views here.

def index(requests):
	if requests.session.has_key('is_logged'):
		return home(requests)
	else:
		return render(requests,'index.html')

def login(requests):
	if requests.method != 'POST':
		return HttpResponseRedirect('/')
	elif requests.method == 'POST':
		user = requests.POST.get('user')
		password = requests.POST.get('password')

	login_validate = Login.objects.filter(Username=user,Password=password)
	if login_validate:
		for e in login_validate:
			account = e.Usertype
		requests.session['is_logged'] = account
		if account == '0':
			return home(requests)
		# return home(requests)
		elif account == '1':
			return HttpResponse('Client Account')
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def home(requests):
	return render(requests,'upload.html')

def upload(requests):
	if requests.method == 'POST':
		img = requests.FILES['picture']
	
	pic = Pics(Picture=img)
	pic.save()
	messages.success(requests,'Saved Successfully...')
	messages.success(requests,'Saved Successfully...')
	return render(requests,'upload.html')

def showimage(requests):
	obj = Pics.objects.all()

	params = {'images':obj}
	return render(requests,'imageshow.html',params)

def delete(requests,picid):
	obj = Pics.objects.filter(pic_id=picid)
	obj.delete()
	messages.success(requests,'Image Deleted')
	return HttpResponseRedirect('/showimage')

def logout(requests):
	if requests.session.has_key('is_logged'):
		del requests.session['is_logged']

		return HttpResponseRedirect('/')