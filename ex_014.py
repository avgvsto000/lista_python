"""
Verifica se a média é menor ou igual a 7, sendo 7 ou acima desse valor exibe "Aprovado", 
caso contrário, exibe "Reprovado".
Caso a média seja igual a 10, exibe "Aprovado com Distinção".
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")