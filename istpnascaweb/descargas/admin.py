from django.contrib import admin
from .models import Download
# Register your models here.
class DownloadAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('name', 'uploadpdf')

admin.site.register(Download, DownloadAdmin)
