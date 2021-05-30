from django.db import models
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField

# Create your models here.

TAGS = (('TECH', 'TECH'), ('JOES', 'JOES'), ('DJANGO', 'DJANGO'), ('REACT', 'REACT'))

class Category(models.Model):
	category_name = models.CharField(max_length=100)

	def __str__(self):
		return self.category_name


class Blog(models.Model):
	category 	= models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	title 		= models.CharField(max_length=100)
	image 		= models.ImageField(upload_to='images')
	content 	= RichTextField()
	extra_title = models.CharField(max_length=100, null=True, blank=True)
	tags 	 	= models.CharField(choices=TAGS, max_length=100, default='TECH')
	is_deleted  = models.BooleanField(default=False)
	created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.title

	class  Meta:   #new
	    verbose_name_plural  =  "Blog"