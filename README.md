# Calculadora de Descontos

Função Python que calcula o desconto de uma compra conforme o valor e a categoria de fidelidade.

## Regras

- Abaixo de R$ 100,00: sem desconto base.
- De R$ 100,00 até menos de R$ 500,00: 10% de desconto base.
- A partir de R$ 500,00: 20% de desconto base.
- Categoria VIP: soma 5 pontos percentuais ao desconto base, sem distinção de maiúsculas, minúsculas ou espaços externos.
- O desconto em dinheiro é limitado a R$ 200,00 e arredondado para centavos.

## Validação

`valor_compra` deve ser numérico, finito e não negativo. `tipo_cliente` deve ser `VIP` ou `COMUM`. Entradas inválidas geram `TypeError` ou `ValueError`, conforme os cenários em `cenarios.txt`.

## Testes

Execute na raiz do projeto:

```powershell
python -m pytest -v
```