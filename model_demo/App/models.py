from distutils.command.upload import upload
import json
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

    def get_skills(self):
        if self.json_text_field == "[]":
            return []
        return json.loads(self.json_text_field)

class Images(models.Model):
    information         = models.ForeignKey(Informations, on_delete=models.CASCADE)
    image               = models.ImageField(upload_to="images")
    created_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.information)



class Quiz(models.Model):
    name            = models.CharField(max_length=10)
    fee             = models.IntegerField(max_length=10, null=True, blank=True)
    discount        = models.CharField(max_length=10, null=True, blank=True)
    start_time      = models.DateTimeField()
    end_time        = models.DateTimeField()

    def __str__(self):
        return str(self.name)


class Option(models.Model):
    content         = models.TextField()
    is_correct      = models.BooleanField()

    def __str__(self):
        return str(self.content)


class Question(models.Model):
    OBJECTIVE = 'OBJ'
    SUBJECTIVE = 'SBJ'
    QUESTION_TYPES = (
        (OBJECTIVE, 'Objective'),
        (SUBJECTIVE, 'Subjective'),
    )
    content         = models.TextField()
    quiz            = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_type   = models.CharField(max_length=3, choices=QUESTION_TYPES, default=OBJECTIVE)
    options         = models.ManyToManyField(Option, related_name='options')

    def __str__(self):
        return str(self.id)