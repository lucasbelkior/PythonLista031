'''
5)	Fazer um programa que pergunte o salário de um funcionário e apresente este salário com um aumento de 15%.
'''
nome = input("Qual é o seu nome?")
print("Ola,",nome,"tudo bem com voce?")
num =int(input("Informe o seu salario por favor:"))
sal = (num*15/100)+num
print("O meu salario e ",num,"com um acrescimo de 15%")
print("entao seu salario e",sal)