#
#? Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Número 1:"))
n2= int(input("Número 2:"))
for n in range(n1+1, n2):
    print(n)