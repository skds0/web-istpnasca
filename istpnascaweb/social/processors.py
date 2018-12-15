from .models import Link

# ctx_dict = diccionario de contexto
def ctx_dict(request):
	ctx = {}
	links = Link.objects.all()
	for link in links:
		ctx[link.key] = link.url
	return ctx
