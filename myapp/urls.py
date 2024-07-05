from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'crear-cuenta'),
    path('categories/', views.categories, name = 'categories'),
    path('news/', views.news, name = 'noticias'),
    path('news-details/', views.newsdetails, name = 'detalles-noticias'),
    path('anime-details/', views.animedetails, name = 'detalles-anime'),
    path('anime-watching/', views.animewatching, name = 'ver-anime'),        
]
