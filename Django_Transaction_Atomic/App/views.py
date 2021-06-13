from django.shortcuts import render, redirect
from django.contrib import messages

from django.db import transaction
from .models import *

# Create your views here.


def index(request):
	if request.method == 'POST':
		try:
			user_one = request.POST.get('user_one')
			user_two = request.POST.get('user_two')
			amount   = request.POST.get('amount')

			# used for commit rollback
			with transaction.atomic():
				user_one_obj = Payment.objects.get(user = user_one.title())
				user_one_obj.amount -= int(amount)
				user_one_obj.save()

				user_two_obj = Payment.objects.get(user = user_two.title())
				user_two_obj.amount += int(amount)
				user_two_obj.save()

				messages.success(request, 'Your amount is transfered')
		except Exception as e:
			print(e)
			messages.error(request, 'Something went wrong')

		return redirect('/')
	return render(request, 'index.html')