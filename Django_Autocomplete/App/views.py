from django.shortcuts import render
from django.http import JsonResponse

from faker import Faker
fake = Faker()
from .models import *


def index(request):
    return render(request, 'index.html')


def generate_data(request):
    for i in range(0 , 100):
        FakeAddress.objects.create(address=fake.address())
    return JsonResponse({'status' : 200})


def search_address(request):
    address = request.GET.get('address')
    payload = []
    if address:
        fake_address_objs = FakeAddress.objects.filter(address__icontains=address)
        
        for fake_address_obj in fake_address_objs:
            payload.append(fake_address_obj.address)


    return JsonResponse({'status' : 200 , 'data' : payload})
