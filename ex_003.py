# Calculadora Simples: pede dois números e realiza cálculos. 
# OBS: Essa calculadora não possui error handling.
print("Insira dois valores abaixo\n")
num1 = int(input("Inserir o primeiro número: "))
num2 = int(input("Inserir o segundo número: "))
somar = num1 + num2
subtrair = num1 - num2
multiplicar = num1 * num2
dividir = num1 / num2 
print(f"O resultado da soma: {somar}")
print(f"O resultado da subtração: {subtrair}")
print(f"O resultado da multiplicação: {multiplicar}")
print(f"O resultado da divisão: {dividir}")