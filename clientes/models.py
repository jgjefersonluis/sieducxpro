from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.CharField(max_length=2)
    telefone = models.CharField(max_length=13)
    responsavel = models.CharField(max_length=150)
    pesquisador = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nome