from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.forms import ModelForm

# Create your models here.

class Post(models.Model):
    titulo = models.CharField('titulo', max_length=100, blank= False, null = False)
    subtitulo = models.CharField('subtitulo', max_length=200, blank= False, null = False)
    descripcion = models.CharField('descripcion', max_length=150, blank= False, null = False)
    contenido= RichTextField()
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    fecha= models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)
    img= models.URLField()
    

    class Meta:
        verbose_name= 'Post'
        verbose_name_plural= 'Posts'

    def __str__(self):
        return self.titulo



class Avatar(models.Model):
    img= models.ImageField(upload_to="avatars")
    user= models.ForeignKey(User, on_delete= models.CASCADE)


class CrearPostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
    
    
    
    
    '''titulo = models.CharField('titulo', max_length=100, blank= False, null = False)
    subtitulo = models.CharField('subtitulo', max_length=200, blank= False, null = False)
    descripcion = models.CharField('descripcion', max_length=150, blank= False, null = False)
    contenido= RichTextField()
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    fecha= models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)
    img= models.URLField()'''

    