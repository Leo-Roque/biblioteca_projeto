from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo
