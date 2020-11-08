from django.db import models

# Create your models here.
class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50, default=None)
    url = models.CharField(max_length=100)
    descripcion = models.CharField(max_length= 300)
    imagen = models.ImageField(upload_to='Animal')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)


