from django.db import models

# Create your models here.
class Produto(models.Model):
    descricao  = models.CharField(max_length=255)
    codigo = models.IntegerField()
    tipoDeItem  = models.ForeignKey('tipoItemProduto', related_name='tipodeitem', on_delete=models.CASCADE)
    unidade =  models.ForeignKey('unidadeProduto', related_name='unidade', on_delete=models.CASCADE)
    categoria =  models.ForeignKey('categoriaProduto', related_name='unidade', on_delete=models.CASCADE)
    subcategoria =  models.ForeignKey('subcategoriaProduto', related_name='unidade', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
    tags = models.CharField(max_length=25)
    codigoInterno = models.CharField(max_length=25)
    codigoBalanca = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='produtopy')
    def __str__(self):
       return f"{self.nome}, codigo: {self.codigo}"

class unidadeProduto(models.Model):
    unidadereferente = models.CharField(max_length=22)
    def __str__(self):
       return f"{self.unidadereferente}"

class tipoItemProduto(models.Model):
    tipoDeItem = models.CharField(max_length=22)
    def __str__(self):
       return f"{self.tipoDeItem}"

class categoriaProduto(models.Model):
    categoriaReferente = models.CharField(max_length=22)
    def __str__(self):
       return f"{self.categoriaReferente}, {self.subcategoriaReferente}"

class subcategoriaProduto(models.Model):
    subcategoriaReferente = models.CharField(max_length=22)
    def __str__(self):
       return f"{self.subcategoriaReferente}"

class ProdutoEstoque(models.Model):
    movimentarEstoque = models.BooleanField()
    movimentarEstoqueCompisicao = models.BooleanField()
    produtoReferente = models.ForeignKey('Produto', related_name='produtoReferente', on_delete=models.CASCADE)
    custo = models.DecimalField(max_digits=6, decimal_places=2)
    quantidadeProdutoReferente = models.IntegerField()
    def __str__(self):
       return f"{self.produtoReferente}, quantidade: {self.quantidadeProdutoReferente}, custo: {self.quantidadeProdutoReferente}"


