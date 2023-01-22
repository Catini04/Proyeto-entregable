from django.shortcuts import render

# Create your views here.



def mensajes(request):
    return render(request, 'Mensajeria/mensajes.html')
