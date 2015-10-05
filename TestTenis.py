# -*- coding: utf-8 -*-
import unittest
from Tennis import Tennis
"""Permite  Probar el codigo de prueba.py usando unit test"""


class TestTennis(unittest.TestCase):

    def setUp(self):
        self.tenis = Tennis()

    def test_prueba1(self):
        resultado = self.tenis.anoto(15, 0)
        self.assertEqual('Jugador 1 15 Jugador 2 0', resultado)

    def test_prueba2(self):
        resultado = self.tenis.anoto(30, 0)
        self.assertEqual('Jugador 1 30 Jugador 2 0', resultado)

    def test_prueba3(self):
        resultado = self.tenis.anoto(40, 40)
        self.assertEqual('Deuce', resultado)

    def test_prueba4(self):
        resultado = self.tenis.anoto(40, 50)
        self.assertEqual('Advantage Jugador 2', resultado)

if __name__ == "__main__":
    unittest.main()
