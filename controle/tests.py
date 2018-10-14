from django.test import TestCase

from controle.models import Fornecedor

class FornecedorTestCase(TestCase):
    def setUp(self):
        self.fornecedor01 = Fornecedor.objects.create(
                                                        nome='Shopping Mucuripe', 
                                                        endereco='Av. Principal',
                                                        cidade='Fortaleza',
                                                        uf='CE',
                                                        telefone='20202020',
                                                        )

