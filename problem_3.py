soma = 0 

while True:
    numero = int(input("digite um numero (0 para finalizar): "))
    if numero == 0 :
        break

    soma += numero

print(f"{soma}")