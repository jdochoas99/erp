from django.db import models
from produto.models import Produto
# Create your models here.
class venda(models.Model):
    produtoReferentevenda = models.ForeignKey('produto.Produto', related_name='produtoReferentevenda', on_delete=models.CASCADE)
    precovendaVarejo = models.DecimalField(max_digits=6, decimal_places=2)
    precovendaAtacado = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
       return f"produto:{self.produtoReferentevenda}, preço varejo: {self.precovendaVarejo}, venda atacado: {self.precovendaAtacado}"
