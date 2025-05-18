#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários
#superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%
salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250:
    print(f'O salário agora será de R${salario * 1.10}')
else:
    print(f'O salário agora será de R${salario * 1.15}')