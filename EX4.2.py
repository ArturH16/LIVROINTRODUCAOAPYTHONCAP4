#ESCREVA UM PROGRAMA QUE PERGUNTE A VELOCIDADE DO CARRO DE UM USUÁRIO. CASO ULTRAPASSE 80 KM/H, EXIBA UMA MENSAGEM DIZENDO QUE O USUÁRIO FOI MULTADO. NESSE CASO, EXIBA O VALOR DA MULTA, COBRANDO R$ 5 POR KM ACIMA DE 80 KM/H
velocidade = float(input('Qual a velocidade do carro?: '))
if velocidade > 80:
    print(f'VOCÊ FOI MULTADO EM R${5 * (velocidade - 80)}')

