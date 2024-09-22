"""
Programa que pergunta quanto você:
    - ganha por hora
    - o número de horas trabalhadas no mês
Em seguida, calcula e mostra o total do seu salário no referido mês.
"""

salario_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas_mes = float(input("Digite quantas horas você trabalhou esse mês: "))

salario_total = salario_hora * horas_trabalhadas_mes

print(f"Ganhando R${salario_hora:.2f} a hora, tendo trabalhado {horas_trabalhadas_mes} horas no mês, seu salário este mês é de R${salario_total:.2f}.")

"""
Para calcular o salário por hora a partir do salário mensal, reescreva o código dessa forma:

salario_total = float(input("Insira seu salário mensal: "))
horas_trabalhadas_mes = int(input("Insira as suas horas trabalhadas mensalmente: "))

salario_hora = salario_total / horas_trabalhadas_mes

print(f"Você ganha R${salario_hora:.2f} por hora.")

"""