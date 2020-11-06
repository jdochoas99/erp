from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Produto)
admin.site.register(unidadeProduto)
admin.site.register(tipoItemProduto)
admin.site.register(ProdutoEstoque)
admin.site.register(categoriaProduto)
admin.site.register(subcategoriaProduto)
