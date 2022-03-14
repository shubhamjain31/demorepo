from django.shortcuts import render, redirect

from .models import *
import datetime, json

# Create your views here.

def index(request):
    if request.method == "POST":
        title                    = request.POST.get('title')
        
        MyModel.objects.create(title=title, start_time=datetime.datetime.now())
    return render(request, 'index.html')


def information(request):
    if request.method == "POST":
        information_name                = request.POST.get('information_name')
        skills                          = request.POST.getlist('skills')
        images                          = request.FILES.getlist('images')
        print(images)

        information_obj = Informations.objects.create(information_name=information_name)

        count = 1
        skills_list = []

        for skill in skills:
            skills_list.append({str(count): skill})
            count += 1

        information_obj.json_text_field = json.dumps(skills_list)
        information_obj.save()

        for image in images:
            Images.objects.create(information=information_obj, image=image)

        
        return redirect('/information/')
    return render(request, 'information.html')


def show_info(request, id):
    context = {}
    try:
        information_obj = Informations.objects.get(id = id)
        images = Images.objects.filter(information=information_obj)
        context['information_obj'] = information_obj
        context['images'] = images

    except Exception as e:
        print(e)

    return render(request, 'show_information.html', context)