from django.urls import path
from .import views


urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.index, name='index'),  #  rendering ide page
    path('plag', views.ide, name='plag'),   #  response to ide

    path('plagren', views.plaren, name='plaren'),  #  rendering plag
    path('plares', views.plares, name='plares'),  #  response to plag

    path('wikiren', views.wikiren, name='wikiren'),  #  rendering to wiki.html
    path('wikires', views.wikires, name='wikires'),  #  response to wiki.html

    path('docren', views.docren, name='docren'),  #  rendering to doc.html
    path('docres', views.docres, name='docres'),
]
