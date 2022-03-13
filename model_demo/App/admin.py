from django.contrib import admin
from .models import *

# Register your models here.

class MyModelsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on', 'date_created')

admin.site.register(MyModel, MyModelsAdmin)
admin.site.register(Informations)
admin.site.register(Images)