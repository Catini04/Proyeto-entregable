from django.urls import path    
from BlogPersonalApp.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name= "inicio"),


    path('profile/', perfil, name= "perfil"),
    path('editarPerfil/', editarPerfil, name="EditarPerfil"),


    path('blog/', blog, name= "blog"),


    path('aboutme/', aboutme, name= "aboutme"),
    

    path('messages/', mensajes, name= "mensajes"),

    path('registro/', registro, name= "Registro"),
    path('login/', loginview, name= "Login"),
    path('logout/', LogoutView.as_view(), name= "logout"),
    


    
]