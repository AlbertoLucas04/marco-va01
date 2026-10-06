import unittest

from desconto import calcular_desconto


class CalcularDescontoTests(unittest.TestCase):
	def test_compra_abaixo_de_100_nao_recebe_desconto_base(self):
		self.assertEqual(calcular_desconto(99.99, "COMUM"), 0.0)

	def test_compra_de_100_recebe_10_porcento(self):
		self.assertEqual(calcular_desconto(100, "COMUM"), 10.0)

	def test_compra_abaixo_de_500_recebe_10_porcento(self):
		self.assertEqual(calcular_desconto(499.99, "COMUM"), 50.0)

	def test_compra_de_500_recebe_20_porcento(self):
		self.assertEqual(calcular_desconto(500, "COMUM"), 100.0)

	def test_cliente_vip_recebe_acrescimo_sem_desconto_base(self):
		self.assertEqual(calcular_desconto(50, "VIP"), 2.5)

	def test_categoria_vip_ignora_maiusculas_e_minusculas(self):
		self.assertEqual(calcular_desconto(200, "vip"), 30.0)
		self.assertEqual(calcular_desconto(200, "Vip"), 30.0)

	def test_cliente_comum_nao_recebe_acrescimo(self):
		self.assertEqual(calcular_desconto(200, "COMUM"), 20.0)

	def test_desconto_maximo_e_limitado_a_200_reais(self):
		self.assertEqual(calcular_desconto(1000, "COMUM"), 200.0)
		self.assertEqual(calcular_desconto(2000, "VIP"), 200.0)


if __name__ == "__main__":
	unittest.main()
