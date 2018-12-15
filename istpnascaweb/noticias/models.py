from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Career(models.Model):
	name = models.CharField(max_length=50, verbose_name="Nombre")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

	class Meta:
		verbose_name = "carrera"
		verbose_name_plural = "carreras"
		ordering = ['-created']

	def __str__(self):
		return self.name	

class Post(models.Model):
	title = models.CharField(max_length=150, verbose_name="Titulo")
	content = RichTextField(verbose_name="Contenido")
	published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
	image = models.ImageField(verbose_name="Imagen", upload_to="noti", null=True, blank=True)
	author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
	position = models.CharField(max_length=50, verbose_name="Posición")
	Careers = models.ManyToManyField(Career, verbose_name="Carreras")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
	

	class Meta:
		verbose_name = "entrada"
		verbose_name_plural = "entradas"
		ordering = ['-created']

	def __str__(self):
		return self.title
