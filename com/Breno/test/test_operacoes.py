from unittest import TestCase
from com.Breno.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()
    
    def test_subtracao(self):
        self.assertEqual(self.operacoes.subtracao([10, 5]), 9, "Deveria ser 5")