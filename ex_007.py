"""
Programa que calcula a área de um quadrado, 
em seguida mostra o dobro desta área.
"""

lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2 
dobro = area * 2
print(f"O dobro da área de um quadrado de lado {lado:.2f}m é: {dobro:.2f}m²")