from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^autores/$',views.autor_list),
    url(r'^autores/(?P<pk>[0-9]+)/$',views.autor_detail),
    url(r'^libros/$',views.libro_list),
    url(r'^libros/(?P<pk>[0-9]+)/$',views.libro_detail),
    #url(r'^usuarios/$',views.usuario_list),
    #url(r'^usuarios/(?P<pk>[0-9]+)/$',views.usuario_detail),
    #url(r'^prestamos/$',views.prestamo_list),
    #url(r'^prestamos/(?P<pk>[0-9]+)/$',views.prestamo_detail),
]
