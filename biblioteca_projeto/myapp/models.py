from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    publicado_em = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Editora(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
