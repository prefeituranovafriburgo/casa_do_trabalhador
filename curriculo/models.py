from django.db import models
from autenticacao.models import Pessoa
# Create your models here.

class Educacao(models.Model):
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.curso} em {self.instituicao} ({self.periodo})"


class ExperienciaProfissional(models.Model):
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.cargo} na {self.empresa} ({self.periodo})"