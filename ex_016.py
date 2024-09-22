"""
Gerador de tabuada.
O usuário deve informar de qual numero ele deseja ver a tabuada.
"""
numero = int(input("Digite um numero de 1 a 10: "))
for i in range(1, 10): 
    print(f"{numero} X {i} = {numero * i}")