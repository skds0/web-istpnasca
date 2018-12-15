"""istpnascaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('nosotros', views.about, name="about"),
    path('carreras', views.grade, name="grade"),
    path('computacion', views.computer, name="computer"),
    path('mecanica', views.car, name="car"),
    path('Agropecuaria', views.plant, name="plant"),
    path('guia-de-turismo', views.travel, name="travel"),
    path('enfermeria', views.nurse, name="nurse"),
    path('electrotecnia', views.light, name="light"),
    path('contabilidad', views.book, name="book"),
    path('electronica', views.radio, name="radio"),
    path('transparencia', views.transparent, name="transparent"),
    path('galeria', views.gallery, name="gallery"),
    path('descargas', views.download, name="download"),
    path('contactos', views.contact, name="contact"),
    # url de noticia
    path('noticia/', include('noticias.urls')),
    # url del admin
    path('jet/', include('jet.urls')), # jet URLS
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)