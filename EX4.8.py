#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você
#deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação
#solicitada.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while True:
    operacao = int(input('Qual operação você deseja realizar?\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n Sua escolha: '))
    if operacao == 1:
        print(f'A soma entre os valores {n1} e {n2} resultou em {n1 + n2}')
        break
    elif operacao == 2:
        print(f'A subtração entre os valores {n1} e {n2} resultou em {n1 - n2}')
        break
    elif operacao == 3:
        print(f'A multiplicação entre os valores {n1} e {n2} resultou em {n1 * n2}')
        break
    elif operacao == 4:
        print(f'A divisão entre os valores {n1} e {n2} resultou em {n1 / n2}')
        break
    else:
        print('Por favor, digite uma operação válida!')

