from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    genero = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Sintoma(models.Model):
    descricao = models.CharField(max_length=200)
    intensidade = models.CharField(max_length=50)
    frequencia = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    principio_ativo = models.CharField(max_length=100)
    frequencia = models.CharField(max_length=50)
    prescricao_medica = models.BooleanField()

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class InstituicaoApoio(models.Model):
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    site = models.URLField(blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    fonte = models.CharField(max_length=150)
    data = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.titulo

class AvaliacaoAnsiedade(models.Model):
    data = models.DateField()
    pontuacao = models.IntegerField()
    resultado = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.data} - {self.resultado}"

class AutoAvaliacao(models.Model):
    idade = models.PositiveIntegerField()
    genero = models.CharField(max_length=20)
    respostas = models.TextField()  # pode ser JSON ou texto
    pontuacao = models.IntegerField()

    def __str__(self):
        return f"Autoavaliação {self.id}"

class Alerta(models.Model):
    tipo = models.CharField(max_length=100)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.data_envio.strftime('%Y-%m-%d')}"

class Depoimento(models.Model):
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Depoimento {self.id}"
