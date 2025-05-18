#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a
#quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para
#comércios.
kwh = float(input('Quantida de kWh: '))
instalacao = str(input('TIPOS DE RESIDÊNCIA\nC - COMERCIAL\nR - RESIDENCIAL\nI - INDUSTRIAL\nTipo de Instalação: '))
if instalacao in 'Rr':
    if kwh <= 500:
        print(f'O preço a pagar será de R${kwh * 0.40}')
    else:
        print(f'O preço a pagar será de R${kwh * 0.65}')
if instalacao in 'Cc':
    if kwh <= 1000:
        print(f'o preço a pagar será de R${kwh * 0.55}')
    else:
        print(f'O preço a pagar será de R${kwh * 0.60}')
if instalacao in 'Ii':
    if kwh <= 5000:
        print(f'O preço a pagar será de R${kwh * 0.55}')
    else:
        print(f'O preço a pagar será de R${kwh * 0.60}')
