from distutils.command.upload import upload
from django.db import models
from django.utils.timezone import now

#Importamos todos los usuarios registrados en el admin
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    #Esto devulve el orden de creacion del mas reciente
    class Meta:
        ordering = ["-created"]


      #Esto devulve el nombre del proyecto en el admin
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    categories = models.ManyToManyField(Category, related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    #Esto devulve el orden de creacion del mas reciente
    class Meta:
        ordering = ["-created"]


      #Esto devulve el nombre del proyecto en el admin
    def __str__(self):
        return self.title



