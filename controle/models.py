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
    preco = models.FloatField()
    unidades_no_estoque = models.IntegerField()
    unidades_pedidas = models.IntegerField()
    imagem = models.ImageField(
        upload_to='controle/images', null=True, blank=True
    )
    categoria = models.ForeignKey(
        "Categoria",
        on_delete=models.CASCADE,
    )
    fornecedor = models.ForeignKey(
        "Fornecedor",
        on_delete=models.CASCADE
    )