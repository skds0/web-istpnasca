from django.shortcuts import render, HttpResponse
from noticias.models import Post

# Create your views here.

def home(request):
    noticia = Post.objects.all()
    contexto = {'posts':noticia}
    return render (request, 'core/home.html', contexto)

def about(request):
	return render(request, "core/about.html")

def grade(request):
	return render(request, "core/carrera.html")	

def computer(request):
	return render(request, "core/informatica.html")	

def car(request):
	return render(request, "core/mecanica.html")

def plant(request):
	return render(request, "core/agro.html")

def travel(request):
	return render(request, "core/turismo.html")

def nurse(request):
	return render(request, "core/enfermeria.html")

def light(request):
	return render(request, "core/electricos.html")

def book(request):
	return render(request, "core/contabilidad.html")

def radio(request):
	return render(request, "core/tronic.html")

def transparent(request):
	return render(request, "core/transpa.html")

def gallery(request):
	return render(request, "core/gallery.html")

def download(request):
	return render(request, "core/download.html")

def contact(request):
	return render(request, "core/contact.html")	