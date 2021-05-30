from django.contrib import admin
from .models import *
from django.utils.html import format_html

admin.site.site_header  =  "Custom Blog Admin"  
admin.site.site_title  =  "Custom Blog Admin Site"
admin.site.index_title  =  "Custom Blog Admin"

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	# fields = ('title', 'content', 'image')   # include fields
	# exclude = ('image',)   # exclude fields

	readonly_fields = ['photo_tag']		# image readonly

	list_display = ['title', 'less_content', 'image', 'is_deleted', 'extra_title', 'click_me', 'photo_tag']  # display all fields on all objects page

	list_display_links = ('title', 'less_content') # return a link of column

	list_filter = ('is_deleted', 'created_at', ('extra_title', admin.EmptyFieldListFilter))  # filter the particular column
	radio_fields = {'tags': admin.HORIZONTAL} # {'tags': admin.VERTICAL}

	save_on_top = True  # it shows the save button at top

	search_fields = ['category__category_name']  	# search by column
	list_per_page = 3	# 3 object will appear on a single page

	# change the color of the column text
	def less_content (self, obj):
		# return obj.content[:3]
		return format_html(f'<span style="color:red">{obj.content[:10]}</span>')

	# make a link to view
	def click_me(self, obj):
		return format_html(f'<a href="/admin/App/blog/{obj.id}/change/">View</a>')

	# showing an image
	def photo_tag(self, obj):
		return format_html(f'<img src="/media/{obj.image}" style="height:100px;width:100px;">')


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)