from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def news(request):
	posts = Post.objects.all()
	return render(request, "noticias/inicio.html", {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "noticias/noticia.html", {'post':post})
