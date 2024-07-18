from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return render(request, 'sugoianime/index.html')
# Create your views here.
@login_required


def home(request):
    return render(request, 'sugoianime/home.html')

def login(request):    
    return render(request, 'registration/login.html')

def signup(request):
    return render(request, 'registration/signup.html')
@login_required
def categories(request):
    return render(request, 'sugoianime/categories.html')
@login_required
def news(request):
    return render(request, 'sugoianime/news.html')
@login_required
def newsdetails(request):
    return render(request, 'sugoianime/news-details.html')
@login_required
def animedetails(request):
    return render(request, 'sugoianime/anime-details.html')
@login_required
def animewatching(request):
    return render(request, 'sugoianime/anime-watching.html')
@login_required
def crud(request):
    alumnos = sugoianime.objects.all()
    context = {'sugoianime': sugoianime}
    return render(request, 'sugoianime/sugo_list.html', context)
@login_required
def blog(request):
    return render(request, 'sugoianime/blog.html')

def exit(request):
    logout(request)
    return redirect('index')
