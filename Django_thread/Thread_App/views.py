from django.shortcuts import render

# Create your views here.

def mythread(request):
	print('hello')
	return render(request , 'mythread.html' )