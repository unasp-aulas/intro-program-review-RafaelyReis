valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar

meses = anos * 12

prestacaoMensal = valorCasa / meses

limitePrestacao = salario * 0.3

if prestacaoMensal <= limitePrestacao:
  print(f"{prestacaoMensal:.2f}")
   