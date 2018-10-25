from django.test import TestCase

from controle.models import Fornecedor, Cliente, Categoria, Produto

class ProdutoTestCase(TestCase):
    def setUp(self):
        fornecedor01 = Fornecedor.objects.create(
            nome='Shopping Mucuripe', 
            endereco='Av. Principal',
            cidade='Fortaleza',
            uf='CE',
            telefone='20202020',
        )
        categoria01 = Categoria.objects.create(
            nome = 'Blusa Feminina',
            descricao = 'Blusa Descrição'
        )
    
        produto01 = Produto.objects.create(
            descricao = 'Descrição teste Produto',
            preco = 39.0,
            unidades_compradas = 5,
            fornecedor = fornecedor01,
            categoria = categoria01
        )
        

# class ClienteTestCase(TestCase):
#     def setUp(self):
#         self.cliente01 = Cliente.objects.create(
#         nome = 'Leandro',
#         contato = '3014-2855',
#         rua = '11',
#         numero = '440',
#         bairro = 'Novo Maracanau',
#         )
# class CategoriaTestCase(TestCase):
#     def setUp(self):
#         self.categoria01 = Categoria.objects.create(
#             nome = 'Blusa Feminina',
#             descricao = 'Blusa Descrição'
#         )


