from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'sugoianime/home.html')

def login(request):
    return render(request, 'sugoianime/login.html')

def signup(request):
    return render(request, 'sugoianime/signup.html')

def categories(request):
    return render(request, 'sugoianime/categories.html')

def news(request):
    return render(request, 'sugoianime/news.html')

def newsdetails(request):
    return render(request, 'sugoianime/news-details.html')

def animedetails(request):
    return render(request, 'sugoianime/anime-details.html')

def animewatching(request):
    return render(request, 'sugoianime/anime-watching.html')