#9. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

number = int(input('Numero: '))

if number >= 1:
    for i in range(1, number):
        if number % i != 0:
            print(number, 'é primo')
        else:
            print(number, 'não é primo')
            break
elif number == 0:
    print(number, 'é zero')
else:
    print(number, 'é negativo')

