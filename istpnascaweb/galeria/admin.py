from django.contrib import admin
from .models import Gallery

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

admin.site.register(Gallery, GalleryAdmin)	