from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField(
        upload_to='controle/images', null=True, blank=True
    )

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    preco = models.FloatField(default=0.0)
    unidades_compradas = models.IntegerField()
    # unidades_no_estoque = models.IntegerField()
    # imagem = models.ImageField(
    #     upload_to='controle/images', null=True, blank=True
    # )
    categoria = models.ForeignKey(
        "Categoria",
        on_delete=models.CASCADE,
    )
    fornecedor = models.ForeignKey(
        "Fornecedor",
        on_delete=models.CASCADE
    )

    # def qtd_estoque(self):
    #     return self.unidades_no_estoque - self.unidades_pedidas

    def __str__(self):
        return self.descricao


class ItemVendido(models.Model):
    preco_unitario = models.FloatField()
    quantidade = models.IntegerField()
    desconto = models.FloatField()
    data_venda = models.DateField()
    produto = models.ForeignKey(
        "Produto",
        on_delete =models.CASCADE,
    )
    cliente = models.ForeignKey(
        "Cliente",
        on_delete=models.CASCADE,
    )

    # Custom save method in model [ItemVendido]
    def get_preco_produto(self):
        self.preco_unitario = self.produto.preco
    
    def save(self, *args, **kwargs):
        self.get_preco_produto()        
        super(ItemVendido, self).save(*args, **kwargs)

    #Valor do produto se for dado desconto
    def valor_final_prod(self):
        return (self.produto.preco - self.desconto) * self.quantidade

    def __str__(self):
        return str(self.produto)

    # item = ItemVendido.objects.aggregate(valor_total=Avg(F('quantidade')*F('quantidade')))

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    contato = models.CharField(max_length=20)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
