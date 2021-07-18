from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book, BookSerializer, User
import json

# Create your views here.

def index(request):
	return render(request,'index.html')

def save_book(request):
	name  		= request.GET['name']
	prize  		= request.GET['prize']
	pages  		= request.GET['pages']

	book = Book(name=name, prize=prize, pages=pages)
	try:
		book.save()
		return HttpResponse('Saved Successfully')
	except:
		return HttpResponse('Error')

def getAllBooks(request):
	l = list()
	books = Book.objects.all()

	for b in books:
		serializer = BookSerializer(b)
		l.append(serializer.data)
	return HttpResponse(json.dumps(l))

def deletebook(request):
	try:
		bookid 		= request.GET['id']
		book 		= Book.objects.get(id=bookid)
		book.delete()
		return HttpResponse('Delete Successfully')
	except:
		return HttpResponse('Error')

def updatebook(request):
	_id 		= request.GET['id']
	name  		= request.GET['name']
	prize  		= request.GET['prize']
	pages 		= request.GET['pages']

	book = Book.objects.get(pk=_id)
	try:
		book.name  	= name
		book.prize  = prize
		book.pages  = pages
		book.save()
		return HttpResponse('Updated Successfully')
	except:
		return HttpResponse('Error')

def signuppage(request):
	return  render(request,'signuppage.html')

def signup(request):
	name 		= request.GET['name']
	email 		= request.GET['email']
	password 	= request.GET['password']

	user = User(name=name, email=email, password=password)
	user.save()
	return HttpResponse('Saved Successfully')

def checkemail(request):
	email = request.GET['email']
	try:
		user = User.objects.get(email=email)
		return HttpResponse('true')
	except:
		return HttpResponse('false')