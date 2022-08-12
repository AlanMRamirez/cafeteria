from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = RichTextField()
    order = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    #Esto devulve el orden de creacion del mas reciente
    class Meta:
        ordering = ["order","title"]

      #Esto devulve el nombre del proyecto en el admin
    def __str__(self):
        return self.title



