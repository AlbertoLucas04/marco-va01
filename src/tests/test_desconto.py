import pytest

from src.calcDesc.desconto import calcular_desconto


@pytest.mark.parametrize(
	("valor_compra", "tipo_cliente", "desconto_esperado"),
	[
		(99.99, "COMUM", 0.0),
		(100.00, "COMUM", 10.0),
		(100.01, "COMUM", 10.0),
		(200.00, "COMUM", 20.0),
		(499.99, "COMUM", 50.0),
		(500.00, "COMUM", 100.0),
		(500.01, "COMUM", 100.0),
	],
	ids=["abaixo-de-100", "limite-100", "acima-de-100", "faixa-intermediaria", "abaixo-de-500", "limite-500", "acima-de-500"],
)
def test_desconto_base_por_faixa(valor_compra, tipo_cliente, desconto_esperado):
	resultado = calcular_desconto(valor_compra, tipo_cliente)

	assert resultado == desconto_esperado


@pytest.mark.parametrize("tipo_cliente", ["VIP", "vip", "Vip", " vIp "])
def test_vip_recebe_acrescimo_sem_distincao_de_caixa(tipo_cliente):
	valor_compra = 200.00
	resultado_esperado = 30.00

	resultado = calcular_desconto(valor_compra, tipo_cliente)

	assert resultado == resultado_esperado


def test_vip_recebe_acrescimo_mesmo_sem_desconto_base():
	valor_compra = 50.00
	tipo_cliente = "VIP"
	resultado_esperado = 2.50

	resultado = calcular_desconto(valor_compra, tipo_cliente)

	assert resultado == resultado_esperado


def test_cliente_comum_nao_recebe_acrescimo_e_aceita_variacao_de_caixa():
	valor_compra = 200.00
	tipo_cliente = " comum "
	resultado_esperado = 20.00

	resultado = calcular_desconto(valor_compra, tipo_cliente)

	assert resultado == resultado_esperado


@pytest.mark.parametrize(
	("valor_compra", "tipo_cliente"),
	[(1000.00, "COMUM"), (2000.00, "VIP")],
	ids=["no-teto", "acima-do-teto"],
)
def test_desconto_nao_ultrapassa_200_reais(valor_compra, tipo_cliente):
	resultado_esperado = 200.00
	resultado = calcular_desconto(valor_compra, tipo_cliente)

	assert resultado == resultado_esperado


def test_compra_zero_recebe_desconto_zero():
	valor_compra = 0
	tipo_cliente = "COMUM"
	resultado_esperado = 0.00

	resultado = calcular_desconto(valor_compra, tipo_cliente)

	assert resultado == resultado_esperado


@pytest.mark.parametrize("valor_compra", [-0.01, -100.00])
def test_compra_negativa_e_rejeitada(valor_compra):
	tipo_cliente = "COMUM"

	with pytest.raises(ValueError, match="não pode ser negativo"):
		calcular_desconto(valor_compra, tipo_cliente)


@pytest.mark.parametrize("valor_compra", ["100", None, True])
def test_valor_de_compra_nao_numerico_e_rejeitado(valor_compra):
	tipo_cliente = "COMUM"

	with pytest.raises(TypeError, match="deve ser um número"):
		calcular_desconto(valor_compra, tipo_cliente)


@pytest.mark.parametrize("valor_compra", [float("nan"), float("inf"), float("-inf")])
def test_valor_de_compra_nao_finito_e_rejeitado(valor_compra):
	tipo_cliente = "COMUM"

	with pytest.raises(ValueError, match="deve ser finito"):
		calcular_desconto(valor_compra, tipo_cliente)


@pytest.mark.parametrize("tipo_cliente", ["", "   ", "REGULAR"])
def test_categoria_vazia_ou_desconhecida_e_rejeitada(tipo_cliente):
	valor_compra = 200.00

	with pytest.raises(ValueError, match="deve ser 'VIP' ou 'COMUM'"):
		calcular_desconto(valor_compra, tipo_cliente)


@pytest.mark.parametrize("tipo_cliente", [None, 1])
def test_categoria_que_nao_e_texto_e_rejeitada(tipo_cliente):
	valor_compra = 200.00

	with pytest.raises(TypeError, match="deve ser um texto"):
		calcular_desconto(valor_compra, tipo_cliente)
