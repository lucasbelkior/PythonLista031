'''
9)	Fazer um algoritmo que pergunte 1 número e apresente:
a)	O próprio número
b)	O quadrado deste número
c)	A raiz quadrada deste número
'''
import math

nume = int(input("Qual o numero a ser inserido?"))
print("O seu numero e",nume)

print("O quadrado desse numero e", math.pow(nume,2))

print("A raiz quadrada do seu numero e",math.sqrt(nume))
