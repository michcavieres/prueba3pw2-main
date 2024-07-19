from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from .forms import CrudForm
from .models import Media
from django.db import IntegrityError


def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda user: user.is_staff, login_url='/login/')(view_func)
    return decorated_view_func

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
def perfil(request):
    context={"clase": "perfil"}
    return render(request, 'sugoianime/perfil.html', context)
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
def blog(request):
    return render(request, 'sugoianime/blog.html')


@admin_required
def crud(request):
    media = Media.objects.all()
    return render(request, 'sugoianime/crud.html', {'media': media})
@admin_required
def create_crud(request):
    
    if request.method == 'GET':
        return render(request, 'sugoianime/create_crud.html', {
        'form' : CrudForm
    })
    else:
        try:
            form = CrudForm(request.POST, request.FILES )
            new_media = form.save(commit=False)
            new_media.save()
            return redirect('crud')
        except ValueError:
            return render(request, 'create_crud.html', {
                'form' : CrudForm,
                'error' : 'por favor, provea datos validos'
            })
@admin_required
def detail_crud(request, media_id):
    if request.method == 'GET':
        media = get_object_or_404(Media, pk= media_id)
        form = CrudForm(instance=media)
        return render(request, 'sugoianime/detail_crud.html', {'media': media, 'form': form,})
    else:
        try:
            media = get_object_or_404(Media, pk= media_id)
            form = CrudForm(request.POST, request.FILES, instance=media)
            if form.is_valid():
                form.save()
            return redirect('crud')
        except ValueError:
            return render(request, 
                        'sugoianime/detail_crud.html', 
                        {'media': media, 
                        'form': form,
                        'error':'error al modificar archivo'
                        })
@admin_required
def delete_crud(request, media_id):
    media = get_object_or_404(Media, pk=media_id)
    if request.method == 'POST':
        media.delete()
        return redirect('crud')





def exit(request):
    logout(request)
    return redirect('index')
