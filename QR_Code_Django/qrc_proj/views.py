from django.shortcuts import render
from websites.models import Website
import os

def index(request):
    name = "Welcome to"
    
    obj = Website.objects.get(id=2)
    context = {
        'name': name,
        'obj' : obj,
    }

    return render(request, 'home.html', context)
