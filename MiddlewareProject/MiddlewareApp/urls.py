from django.urls import path
from MiddlewareApp import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
