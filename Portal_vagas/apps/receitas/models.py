from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_vaga = models.CharField(max_length=248)
    localizacao = models.CharField(max_length=248)
    descricao = models.TextField()
    salario = models.TextField()          
    date = models.DateTimeField(default=datetime.now, blank=True)    
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo_vaga
