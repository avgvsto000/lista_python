"""
Pede a temperatura em graus Fahrenheit e converte para a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
graus_farenheit = float(input("Digite a temperatura em Farenheit: "))
graus_celsius = 5 * (graus_farenheit - 32) / 9
print(f"{graus_farenheit:.2f} graus Farenheit correspondem a {graus_celsius:.2f} graus Celsius")

"""
Para converter a temperatura de Celius para Fahrenheit:
graus_celsius = float(input("Digite a temperatura em Celsius: "))
graus_farenheit = ((graus_celsius * 9) / 5) + 32
print(f"{graus_celsius:.2f} graus Celsius correspondem a {graus_farenheit:.2f} graus Farenheit")
"""