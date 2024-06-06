from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet, AutorViewSet, EditoraViewSet, CategoriaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register('livros', LivroViewSet)
router.register('autores', AutorViewSet)
router.register('editoras', EditoraViewSet)
router.register('categorias', CategoriaViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
