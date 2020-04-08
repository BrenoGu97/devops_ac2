from unittest import TestCase
from com.Breno.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()
    
    def test_soma(self):
        self.assertEqual(self.operacoes.soma([3, 2]), 4, "retorna 5")