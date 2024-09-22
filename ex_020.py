"""
Calcula o preço de venda com base em uma margem de lucro desejada.
"""
def calcular_preco_venda(custo_compra, margem_lucro):
    """Calcula o preço de venda com base em uma margem de lucro desejada."""
    preco_venda = custo_compra * (1 + margem_lucro / 100)
    return preco_venda

produto = input("Insira o nome do produto: ")
custo_compra = float(input("Insira o custo de compra: "))
margem_lucro = int(input("Insira a margem de lucro desejada: "))
print(f"O preço de venda de um(a) {produto} com margem de lucro de {margem_lucro}% é:\n"
      f"R${calcular_preco_venda(custo_compra, margem_lucro)}.")