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
        return f"nome: {self.nome} cpf: {self.cpf} com o endereço: {self.endereco}, {self.cep}. telefone: {self.telefone}  "


class Produto(models.Model):
    nome  = models.CharField(max_length=255)
    codigo = models.IntegerField()
    tipoDeItem  = models.ForeignKey('tipoItemProduto', related_name='tipodeitem', on_delete=models.CASCADE)
    unidade =  models.ForeignKey('unidadeproduto', related_name='unidadeproduto', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=25)
    custo = models.DecimalField(max_digits=6, decimal_places=2)
    precovendaVarejo = models.DecimalField(max_digits=6, decimal_places=2)
    precovendaAtacado = models.DecimalField(max_digits=6, decimal_places=2)


class unidadeProduto(models.Model):
    unidade = models.CharField(max_length=13)

class tipoItemProduto(models.Model):
    tipoDeItem = models.CharField(max_length=13)
    def __str__(self):
       return f"{self.tipoDeItem}  "