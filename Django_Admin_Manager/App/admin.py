from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	# fields = ('title', 'content', 'image')   # include fields
	# exclude = ('image',)   # exclude fields

	list_display = ['title', 'less_content', 'image', 'is_deleted', 'extra_title', 'click_me']  # display all fields on all objects page

	list_display_links = ('title', 'less_content') # return a link of column

	list_filter = ('is_deleted', 'created_at', ('extra_title', admin.EmptyFieldListFilter))  # filter the particular column
	radio_fields = {'tags': admin.VERTICAL}

	def less_content (self, obj):
		# return obj.content[:3]
		return format_html(f'<span style="color:red">{obj.content[:10]}</span>')

	def click_me(self, obj):
		return format_html(f'<a href="/admin/App/blog/{obj.id}/change/">View</a>')

admin.site.register(Blog, BlogAdmin)