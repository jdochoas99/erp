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

class unidadeProduto(models.Model):
    unidadereferente = models.CharField(max_length=13)
    def __str__(self):
       return f"{self.unidadereferente}"

class tipoItemProduto(models.Model):
    tipoDeItem = models.CharField(max_length=13)
    def __str__(self):
       return f"{self.tipoDeItem}"

class Produto(models.Model):
    nome  = models.CharField(max_length=255)
    codigo = models.IntegerField()
    tipoDeItem  = models.ForeignKey('tipoItemProduto', related_name='tipodeitem', on_delete=models.CASCADE)
    unidade =  models.ForeignKey('unidadeProduto', related_name='unidade', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=25)
    def __str__(self):
       return f"produto:{self.nome}, codigo: {self.codigo}"



class ProdutoEstoque(models.Model):
    produtoReferente = models.ForeignKey('Produto', related_name='produtoReferente', on_delete=models.CASCADE)
    custo = models.DecimalField(max_digits=6, decimal_places=2)
    quantidadeProdutoReferente = models.IntegerField()
    def __str__(self):
       return f"produto:{self.produtoReferente}, quantidade: {self.quantidadeProdutoReferente}, custo: {self.quantidadeProdutoReferente}"

class venda(models.Model):
    produtoReferentevenda = models.ForeignKey('Produto', related_name='produtoReferentevenda', on_delete=models.CASCADE)
    precovendaVarejo = models.DecimalField(max_digits=6, decimal_places=2)
    precovendaAtacado = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
       return f"produto:{self.produtoReferentevenda}, preço varejo: {self.precovendaVarejo}, venda atacado: {self.precovendaAtacado}"
