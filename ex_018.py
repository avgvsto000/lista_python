"""
Calculadora de Troco em Caixa de Loja
"""
print("Caixa de Loja")
total = 0
produto = 0
valor = 0

while True:
    produto += 1
    valor = float(input(f"Produto {produto}: R$ "))
    if valor == 0:
        break
    total += valor

print(f"Total: R$ {total:.2f}")
dinheiro = float(input("Dinheiro: R$ "))
print(f"Troco: R${dinheiro - total:.2f}")