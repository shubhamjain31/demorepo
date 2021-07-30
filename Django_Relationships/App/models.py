from django.db import models

# Create your models here.

class Publisher(models.Model):
    name 	= models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Book(models.Model):
    name 		= models.CharField(max_length=300)
    price 		= models.IntegerField(default=0)
    publisher 	= models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'books'

    def __str__(self):
        return self.name

class Store(models.Model):
    name 		= models.CharField(max_length=300)
    books 		= models.ManyToManyField(Book)

    class Meta:
        default_related_name = 'stores'

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    mobile = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Adhar(models.Model):
    person = models.OneToOneField("Person",on_delete=models.CASCADE)
    signature = models.TextField()
    adhar_no = models.TextField(max_length=100)

    def __str__(self):
        return str(self.person)