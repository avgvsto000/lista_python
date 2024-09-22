"""
Função para calcular quantos dias faltam para aniversário.
"""
def dias_para_aniversario(mes, dia):
    if mes < mes_hoje or (mes == mes_hoje and dia < dia_hoje):
        mes += 12
    return (mes - mes_hoje) * 30 + (dia - dia_hoje)


mes_hoje = int(input("Insira o mês atual: "))
dia_hoje = int(input("Insira o dia de hoje: "))

mes = int(input("Insira o mês de seu aniversário (1-12): "))
dia = int(input("Insira o dia do seu aniversário (1-31): "))

print(f"Faltam {dias_para_aniversario(mes, dia)} dias para seu aniversário!")