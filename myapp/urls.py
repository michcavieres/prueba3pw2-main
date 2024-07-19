from django.urls import path
from .views import index,home,login,categories,news,newsdetails,animedetails,animewatching,crud,blog,exit,registro,perfil


urlpatterns = [
 path('', index, name='index'),
 path('home/', home, name='home'),
 path('login/', login, name='login'),
 path('registro/', registro, name='registro'),
 path('categories/', categories, name='categories'),
 path('perfil/', perfil, name='perfil'),
 path('news/', news, name='news'),
 path('newsdetails/', newsdetails, name='newsdetails'),
 path('animedetails/', animedetails, name='animedetails'),
 path('animewatching/', animewatching, name='animewatching'),
 path('crud/', crud, name='crud'),
 path('blog/', blog, name='blog'),
 path('logout/', exit, name='exit'),
]
