from django.urls import path
from App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/' ,views.register, name="register"),
    path('login/'  , views.login_attempt , name="login"),
    path('logout_attempt/' , views.logout_attempt , name="logout"),
    path('course/<slug>' ,views.view_course , name="course"),
    path('become_pro/' , views.become_pro , name="become_pro"),
    path('charge/' , views.charge , name="charge"),
]
