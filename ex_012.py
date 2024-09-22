"""
Pede um valor e exibe na tela se o valor é positivo, negativo ou não é um número.
"""
try:
    valor = float(input("Digite um valor: "))
    if valor > 0:
        print("O valor é positivo")
    elif valor < 0:
        print("O valor é negativo")
    else:
        print("O valor é zero.")
except ValueError:
    print("Não é um número.")