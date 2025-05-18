#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve
#perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação
#mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a
#comprar dividido pelo número de meses a pagar.
valor_casa = float(input('Qual o valor da casa?: R$'))
salario = float(input('Qual o seu salário?: R$'))
tempo = int(input('Em quantos anos você quer pagar?: '))
prestacao = valor_casa / tempo
if prestacao / salario > 0.3:
    print('Empréstimo recusado!')
else:
    print(f'Empréstimo aprovado!\nVocê pagará uma prestação de {prestacao} por {tempo}')