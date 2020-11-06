from django.db import models

# Create your models here.
class Produto(models.Model):
    descricao  = models.CharField(max_length=255)
    codigo = models.IntegerField()
    tipoDeItem  = models.ForeignKey('tipoItemProduto', related_name='tipodeitem', on_delete=models.CASCADE)
    unidade =  models.ForeignKey('unidadeProduto', related_name='unidade', on_delete=models.CASCADE)
    categoria =    models.ForeignKey('categoriaProduto', related_name='categoria', on_delete=models.CASCADE)
    subcategoria =    models.ForeignKey('subcategoriaProduto', related_name='subcategoria', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
    tags = models.CharField(max_length=25,blank=True)
    codigoInterno = models.CharField(max_length=25,blank=True)
    codigoBalanca = models.CharField(max_length=25,blank=True)
    photo = models.ImageField(upload_to='produtopy',blank=True)
    def __str__(self):
       return f"{self.descricao}, codigo: {self.codigo}"

class unidadeProduto(models.Model):
    unidadereferente = models.CharField(max_length=22)
    def __str__(self):
       return f"{self.unidadereferente}"

class tipoItemProduto(models.Model):
    tipoDeItem = models.CharField(max_length=22)
    def __str__(self):
       return f"{self.tipoDeItem}"

class categoriaProduto(models.Model):
    name = models.CharField(max_length=22)
    def __str__(self):
       return f"{self.name}"

class subcategoriaProduto(models.Model):
    name = models.CharField(max_length=22)
    parent = models.ForeignKey('categoriaProduto', related_name='parent', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"



    # def __str__(self):                           
    #     full_path = [self.name]            
    #     k = self.parent
    #     while k is not None:
    #         full_path.append(k.name)
    #         k = k.parent

    #     return ' -> '.join(full_path[::-1])

class ProdutoEstoque(models.Model):
    movimentarEstoque = models.BooleanField()
    movimentarEstoqueCompisicao = models.BooleanField()
    produtoReferente = models.ForeignKey('Produto', related_name='produtoReferente', on_delete=models.CASCADE)
    custo = models.DecimalField(max_digits=6, decimal_places=2)
    quantidadeProdutoReferente = models.IntegerField()
    def __str__(self):
       return f"{self.produtoReferente}, quantidade: {self.quantidadeProdutoReferente}, custo: {self.quantidadeProdutoReferente}"


