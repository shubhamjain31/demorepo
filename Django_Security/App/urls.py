from django.urls import path
from App import views

app_name = "App"

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    
    path('employees', views.employees, name="employees"),
    path('search_employees', views.search_employees, name='search_employees'),
    
    path('dns_lookup', views.dns_lookup, name='dns_lookup'),
]
