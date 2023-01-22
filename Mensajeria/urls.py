from django.urls import path    
from Mensajeria.views import *
from django.contrib.auth.views import LogoutView

app_name = 'Mensajeria'

urlpatterns = [

path('mensajes/', mensajes, name= 'mensajes'),


]



