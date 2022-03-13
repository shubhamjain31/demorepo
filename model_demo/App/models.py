from distutils.command.upload import upload
from django.db import models

# Create your models here.

# practice on all date fields
class MyModel(models.Model):
    title               = models.CharField(max_length = 200, null=True, blank=True)
    start_time          = models.DateTimeField(null=True, blank=True)
    created_on          = models.DateTimeField(auto_now_add=True)
    updated_on          = models.DateTimeField(auto_now=True)
    date_created        = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

#----------------------------------------------@ practice on multiple images @------------------------------------------------------
class Informations(models.Model):
    information_name         = models.CharField(max_length = 200, null=True, blank=True)
    json_text_field          = models.TextField(default="[]")
    created_at               = models.DateTimeField(auto_now_add=True)
    updated_at               = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.information_name

class Images(models.Model):
    information         = models.ForeignKey(Informations, on_delete=models.CASCADE)
    image               = models.ImageField(upload_to="images")
    created_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.information)