from django.contrib import admin
from .models import Career, Post

# Register your models here.
class CareerAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('title', 'image', 'author', 'published', 'post_careers')	
	ordering = ('author', 'published')
	search_fields = ('title', 'content',)

	def post_careers(self, obj):
		return ", ".join([c.name for c in obj.Careers.all().order_by("name")])

	post_careers.short_description = "Carreras"	
		

admin.site.register(Career, CareerAdmin)
admin.site.register(Post, PostAdmin)
