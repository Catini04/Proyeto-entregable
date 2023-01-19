from django.db import models
from django.contrib.auth.models import User

# Create your models here.



"""class Blog(models.Model):
    titulo = models.CharField()
    subtitulo = models.CharField()
    cuerpo= models.CharField()
    autor= models.CharField()
    fecha= models.DateField()
    img= models.ImageField()"""



class Avatar(models.Model):
    img= models.ImageField(upload_to="avatars")
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    