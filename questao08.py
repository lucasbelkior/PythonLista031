'''
8)	Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o valor do consumo médio do automóvel, em quilômetros por litro.
'''

distancia = float(input("Qual será a distancia percorrida em sua viagem em quilometros?"))
consumo = float(input("Qual é o valor do consumo médio do automóvel, em quilômetros por litro?"))
gasto = distancia/consumo
print(" quantidade gasto em litros na viagem sera:",gasto,"KM/L")
