#
#? Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

import math


def inteiro_decimal(n):
    if n == math.ceil(n):
        return "Inteiro"
    else:
        return "Decimal"

n = float(input("Digite um número:"))
print(f"O número digita é {inteiro_decimal(n)}")