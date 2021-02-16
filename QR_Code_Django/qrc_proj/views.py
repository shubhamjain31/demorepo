from django.shortcuts import render
from websites.models import Website
import os

def index(request):
    name = "Welcome to"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    obj = Website.objects.get(id=2)
    print(os.path.join(os.path.dirname(
    BASE_DIR), "media_root"))

    context = {
        'name': name,
        'obj' : obj,
    }

    return render(request, 'home.html', context)