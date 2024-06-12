valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar

meses = anos_pagar * 12

prestacao_mensal = valor_casa / meses

limite_prestacao = salario * 0.3

if prestacao_mensal <= limite_prestacao:
   