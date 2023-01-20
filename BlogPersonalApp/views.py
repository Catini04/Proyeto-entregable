from django.shortcuts import render, HttpResponse

from .models import *
from BlogPersonalApp.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.



def inicio(request):
    return render(request, 'BlogPersonalApp/inicio.html')

#--------------PERFIL-------------
@login_required
def perfil(request):
    
    return render(request, 'BlogPersonalApp/perfil.html')

@login_required
def editarPerfil(request):
    usuario= request.user
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email= info["email"]
            usuario.password1= info["password1"]
            usuario.password2 =info["password2"]
            usuario.first_name= info["first_name"]
            usuario.last_name= info["last_name"]
            usuario.save()
            return render(request, 'BlogPersonalApp/inicio.html', {"mensaje": "Usuario modificado"})
        else:
            return render(request, 'BlogPersonalApp/editarPerfil.html', {'form': form})
    else:
        form = EditarPerfilForm(instance= usuario)
        return render(request, 'BlogPersonalApp/editarPerfil.html', {'form': form, 'nombredeusuario': usuario.username})



"""def obtenerAvatar(request):
    lista= Avatar.objects.filter(user=request.user)
    if len(lista) != 0:
        avatar= lista[0].imagen.url
    else:
        avatar= '/media/avatars/defectoavatar.jpg'
    return avatar"""
 





@login_required
def blog(request):
    posts= Post.objects.filter()
    return render(request, 'BlogPersonalApp/blog.html', {'posts': posts})

@login_required
def leerPost(request, subtitulo):
    post =  Post.objects.get(subtitulo= subtitulo)
    return render(request, 'BlogPersonalApp/leerPost.html', {'post': post})

@login_required
def crearPost(request):
    if request.method == 'POST':
        form = CrearPostForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            post = Post ( 
            titulo = info['titulo'],
            subtitulo = info['subtitulo'],
            descripcion = info['descripcion'],
            contenido = info['contenido'],
            autor= info['autor'],
            
            img= info['img'],
            )
            post.save()
            return render(request, 'BlogPersonalApp/inicio.html')
        else: 
            return render(request, 'BlogPersonalApp/crearPost.html', {'form': form})
    else: 
        form = CrearPostForm()
        return render(request, 'BlogPersonalApp/crearPost.html', {'form': form})




def aboutme(request):
    return render(request, 'BlogPersonalApp/aboutme.html')



@login_required
def mensajes(request):
    return render (request, 'BlogPersonalApp/mensajes.html')



#-----------REGISTRO Y LOGIN------------

def registro(request):
    if request.method == 'POST':
        form= RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, 'BlogPersonalApp/inicio.html', {"mensaje": f"Usuario {username} creado correctamente"})
        else:
            return render(request, 'BlogPersonalApp/registro.html', {"form": form, "mensaje": "Error al crear usuario"})
    else:
        form= RegistrarUsuarioForm()
        return render(request, 'BlogPersonalApp/registro.html', {'form': form})


def loginview(request):
    if request.method== 'POST':
        form= AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            info= form.cleaned_data
            usu= info["username"]
            clav=info["password"]
            usuario= authenticate(username=usu, password=clav)
            if usuario is not None: 
                login(request, usuario)
                return render(request, 'BlogPersonalApp/inicio.html', {"mensaje": f"Bienvenido, {usuario}, se ha logueado correctamente"})
            else:
                return render(request, 'BlogPersonalApp/login.html', {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, 'BlogPersonalApp/login.html', {"form": form, "mensaje": "Usuario o contraseña incorrectos"})

    else: 
        form= AuthenticationForm()
        return render(request, 'BlogPersonalApp/login.html',{'form': form})




#-----------------------------CRUD DEL BLOG-----------------------------------



    