from django.contrib import admin
from . models import Produto, Categoria, Fornecedor, ItemVendido, Cliente

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(ItemVendido)
admin.site.register(Cliente)