from django.db import models

# Create your models here.
class Produto(models.Model):
    nome  = models.CharField(max_length=255)
    codigo = models.IntegerField()
    tipoDeItem  = models.ForeignKey('tipoItemProduto', related_name='tipodeitem', on_delete=models.CASCADE)
    unidade =  models.ForeignKey('unidadeProduto', related_name='unidade', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=25)
    def __str__(self):
       return f"{self.nome}, codigo: {self.codigo}"

class unidadeProduto(models.Model):
    unidadereferente = models.CharField(max_length=13)
    def __str__(self):
       return f"{self.unidadereferente}"

class tipoItemProduto(models.Model):
    tipoDeItem = models.CharField(max_length=13)
    def __str__(self):
       return f"{self.tipoDeItem}"


class ProdutoEstoque(models.Model):
    produtoReferente = models.ForeignKey('Produto', related_name='produtoReferente', on_delete=models.CASCADE)
    custo = models.DecimalField(max_digits=6, decimal_places=2)
    quantidadeProdutoReferente = models.IntegerField()
    def __str__(self):
       return f"{self.produtoReferente}, quantidade: {self.quantidadeProdutoReferente}, custo: {self.quantidadeProdutoReferente}"
