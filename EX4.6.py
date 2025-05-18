#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o
#preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais
#longas.
distancia = float(input('Digite a distância que será percorrida em Km: '))
if distancia <= 200:
    print(f'Você pagará R${0.5*distancia}')
else:
    print(f'Você pagará R${0.45*distancia}')