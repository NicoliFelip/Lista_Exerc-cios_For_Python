#5. Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
numero= int(input("digite um numero para que seja feita sua tabuada até o 10:  "))

for i in range (1,11):
  tabuada= numero *(i)
  contador= i + 1
  print (f"{numero} x {contador} = {tabuada}")