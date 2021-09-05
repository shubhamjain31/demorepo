"""Django_ORM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('add/student/', add_student, name='add_student'),
    path('add/teacher/', add_teacher, name='add_teacher'),
    path('add/classroom/', add_classroom, name='add_classroom'),
    path('add/courses/', add_courses, name='add_courses'),
    path('add/grade/', add_grade, name='add_grade'),

    path('edit/student/<int:id>', edit_student, name='edit_student'),
    path('edit/teacher/<int:id>', edit_teacher, name='edit_teacher'),
    path('edit/classroom/<int:id>', edit_classroom, name='edit_classroom'),
    path('edit/courses/<str:val>', edit_courses, name='edit_courses'),

]
