#Escreva um programa que leia três números e que imprima o maior e o menor
maior = menor = 0
for c in range(0,3):
    n = float(input(f'Digite o {c+1} número: '))
    if c == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
           menor = n
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')