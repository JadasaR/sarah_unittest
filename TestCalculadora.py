# -*- coding: utf-8 -*-
import unittest
from Calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_suma_de_2_mas_2(self):
        resultado = self.calc.suma(2, 2)
        self.assertEqual(4, resultado)

    def test_suma_de_3_mas_3(self):
        resultado = self.calc.suma(3, 3)
        self.assertEqual(6, resultado)

    def test_resta_de_2_menos_2(self):
        resultado = self.calc.resta(2, 2)
        self.assertEqual(0, resultado)

    def test_resta_de_3_menos_3(self):
        resultado = self.calc.resta(3, 3)
        self.assertEqual(0, resultado)

if __name__ == "__main__":
    unittest.main()
