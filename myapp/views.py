from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

def index(request):
    return render(request, 'sugoianime/index.html')
# Create your views here.
@login_required


def home(request):
    return render(request, 'sugoianime/home.html')

def login(request):    
    return render(request, 'registration/login.html')



def registro(request):
    if request.method != "POST":
        context={"clase": "registro"}
        return render(request, 'registration/registro.html', context)
    else:
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(nombre, email, password)
        user.save()
        context={"clase": "registro", "mensaje":"Los datos fueron registrados"}
        return render(request, 'registration/registro.html', context)
    
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
