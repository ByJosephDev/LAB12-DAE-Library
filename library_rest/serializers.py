from rest_framework import serializers
from .models import *

class AutorSerializer(serializers.Serializer):

    class Meta:
        model = Autor
        fields = {'id_autor','nombre','nacionalidad'}

    id_autor = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=100)
    nacionalidad = serializers.CharField(max_length=50)

    def create(self,validated_data):
        
        return Autor.objects.create(**validated_data)
    
    def update(self,instance,validated_data):

        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.nacionalidad = validated_data.get('nacionalidad',instance.nacionalidad)
        instance.save()
        return instance
    
class LibroSerializer(serializers.Serializer):

    class Meta:
        model = Libro
        fields = {'id_libro','codigo','titulo','isbn','num_pags','editorial','libro_id_autor_id'}

    id_libro = serializers.IntegerField(read_only=True)
    codigo = serializers.IntegerField(default=0)
    titulo = serializers.CharField(max_length=30)
    isbn = serializers.CharField(max_length=30)
    editorial = serializers.CharField(max_length=60)
    num_pags = serializers.IntegerField(read_only=True)
    libro_id_autor_id = serializers.IntegerField(read_only=True)

    
    def create(self,validated_data):

        return Libro.objects.create(**validated_data)
    
    def update(self,instance,validated_data):

        instance.codigo = validated_data.get('codigo',instance.codigo)
        instance.titulo = validated_data.get('titulo',instance.titulo)
        instance.isbn = validated_data.get('isbn',instance.isbn)
        instance.num_pags = validated_data.get('num_pags',instance.num_pags)
        instance.editorial = validated_data.get('editorial',instance.editorial)
        instance.libro_id_autor_id = validated_data.get('libro_id_autor_id',instance.libro_id_autor_id)        
        instance.save()
        return instance


        