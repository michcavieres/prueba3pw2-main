from django.urls import path
from .views import index,home,login,signup,categories,news,newsdetails,animedetails,animewatching,crud,blog,exit,registro


urlpatterns = [
 path('', index, name='index'),
 path('home/', home, name='home'),
 path('login/', login, name='login'),
 path('signup/', signup, name='signup'),
 path('registro/', registro, name='registro'),
 path('categories/', categories, name='categories'),
 path('news/', news, name='news'),
 path('newsdetails/', newsdetails, name='newsdetails'),
 path('animedetails/', animedetails, name='animedetails'),
 path('animewatching/', animewatching, name='animewatching'),
 path('crud/', crud, name='crud'),
 path('blog/', blog, name='blog'),
 path('logout/', exit, name='exit'),
]
