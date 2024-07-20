from django.urls import path
from .views import index,home,login,categories,news,newsdetails,animedetails,animewatching,crud,blog,exit,registro,perfil,create_crud,detail_crud, delete_crud


urlpatterns = [
 path('', index, name='index'),
 path('home/', home, name='home'),
 path('login/', login, name='login'),
 path('registro/', registro, name='registro'),
 path('categories/', categories, name='categories'),
 path('perfil/', perfil, name='perfil'),
 path('news/', news, name='news'),
 path('newsdetails/', newsdetails, name='newsdetails'),
 path('categories/animedetails/', animedetails, name='animedetails'),
 path('categories/animewatching/', animewatching, name='animewatching'),
 path('crud/', crud, name='crud'),
 path('crud/create/', create_crud, name = 'create_crud'),
 path('crud/<int:media_id>/',detail_crud, name = 'detail_crud'),
 path('crud/<int:media_id>/',delete_crud, name = 'delete_crud'),
 path('blog/', blog, name='blog'),
 path('logout/', exit, name='exit'),
 
]
