"""
Pede uma número, entre zero e dez.
Mostra uma mensagem caso o valor seja inválido 
e continua pedindo até que o usuário informe um valor válido.
"""
num = float(input("Digite uma número de 0 a 10: "))
while num > 10 or num < 0:
    num = float(input("Valor Inválido\nDigite uma número de 0 a 10: "))