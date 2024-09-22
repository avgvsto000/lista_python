"""
Calculadora de Margem de Lucro
"""
receita = float(input("Insira a receita: "))
custos = float(input("Insira os custos: "))

lucro = receita - custos
margem = lucro / receita * 100

print(f"Receita: R${receita:.2f}")
print(f"Custos: R${custos:.2f}")
print(f"A margem de lucro é: {margem:.2f}%")