from django.urls import path  
from App import views  

urlpatterns = [  
    path('', views.index, name='index'),  
    path('add',views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='delete'),
]  