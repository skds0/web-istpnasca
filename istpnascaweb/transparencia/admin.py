from django.contrib import admin
from .models import MyFile
# Register your models here.
class MyFileAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('name', 'uploadpdf')

admin.site.register(MyFile, MyFileAdmin)	

