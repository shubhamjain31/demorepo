from django.contrib import admin
from App.models import Employee, Blog, test_employee,test_blog

# Register your models here.

admin.site.register(Employee)
admin.site.register(Blog)
admin.site.register(test_employee)
admin.site.register(test_blog)
