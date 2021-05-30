from django.db import models

# Create your models here.

TAGS = (('TECH', 'TECH'), ('JOES', 'JOES'), ('DJANGO', 'DJANGO'), ('REACT', 'REACT'))

class Blog(models.Model):
	title 		= models.CharField(max_length=100)
	image 		= models.ImageField(upload_to='images')
	content 	= models.TextField()
	extra_title = models.CharField(max_length=100, null=True, blank=True)
	tags 	 	= models.CharField(choices=TAGS, max_length=100, default='TECH')
	is_deleted  = models.BooleanField(default=False)
	created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.title