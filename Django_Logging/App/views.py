from django.shortcuts import render
from django.http import JsonResponse
import logging, traceback

logger = logging.getLogger('django')

# Create your views here.


def addUser(request):
	val = {"response": "User Added"}
	logger.info('>>>>>>>>>>>>>> Something Debug wrong!')
	return JsonResponse(val, status=200)

def addSomething(request):
	val = {"response": "Somthing Added"}
	return JsonResponse(val, status=200)

def addNew(request, someNumber):
	val = {"response": "Something Added New", "numberGiven":int(someNumber)}
	if int(someNumber)>50:
		return JsonResponse(val, status=500)
	else:
		return JsonResponse(val, status=200)

def addNewError(request, someNumber):
	val = {"response": "Something Added New", "numberGiven":int(someNumber)}
	try:
		if int(someNumber)>50:
			return JsonResponse(val, status=500)
		else:
			return JsonResponse(val, status=200)
	except Exception as e:
		print(str(e).traceback.format_exc())