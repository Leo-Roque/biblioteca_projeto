from django.contrib import admin
from .models import Livro, Autor, Editora, Categoria, Usuario

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Categoria)
admin.site.register(Usuario)
