from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Autor,Libro
from .serializers import AutorSerializer,LibroSerializer

# Create your views here.

class JSONResponse(HttpResponse):

    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

@csrf_exempt
def autor_list(request):
    if request.method=='GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores,many=True)
        return JSONResponse(serializer.data)
    elif request.method=='POST':
        data= JSONParser().parse(request)
        serializer=AutorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.erros,status=400)

@csrf_exempt
def autor_detail(request,pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=='GET':
        serializer = AutorSerializer(autor)
        return JSONResponse(serializer.data)
    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = AutorSerializer(autor,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)
    elif request.method=='DELETE':
        autor.delete()
        return HttpResponse(status=204)

@csrf_exempt
def libro_list(request):
    if request.method=='GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros,many=True)
        return JSONResponse(serializer.data)
    elif request.method=='POST':
        data= JSONParser().parse(request)
        serializer=LibroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.errors,status=400)

@csrf_exempt
def libro_detail(request,pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=='GET':
        serializer = LibroSerializer(libro)
        return JSONResponse(serializer.data)
    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(libro,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)
    elif request.method=='DELETE':
        libro.delete()
        return HttpResponse(status=204)

        