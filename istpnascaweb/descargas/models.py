from django.db import models

# Create your models here.
class Download(models.Model):
	name = models.CharField(max_length=150, verbose_name="Nombre")
	uploadpdf = models.FileField(verbose_name="Archivo", upload_to="descargo")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
	

	class Meta:
		verbose_name = "entrada"
		verbose_name_plural = "entradas"
		ordering = ['-created']

	def __str__(self):
		return self.name