from rest_framework import viewsets
from .models import Livro, Autor, Editora, Categoria, Usuario
from .serializers import LivroSerializer, AutorSerializer, EditoraSerializer, CategoriaSerializer, UsuarioSerializer
from django.http import HttpResponse

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def home(request):
    return HttpResponse("Bem-vindo à Biblioteca!")
