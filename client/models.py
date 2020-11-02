from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=25)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    ddd = models.IntegerField()
    telefone = models.IntegerField()
    def __str__(self):
        return f"nome: {self.nome} cpf: {self.cpf} com o endereço: {self.endereco}, {self.cep}. telefone: {self.telefone}"
