from django.db import models

# Create your models here.

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

class Libro(models.Model):

    id_libro = models.AutoField(primary_key=True)
    codigo = models.IntegerField(default=0)
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    num_pags = models.IntegerField(default=0)
    libro_id_autor = models.ForeignKey(Autor,null=True,blank=True,on_delete=models.CASCADE)

    