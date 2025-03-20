numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 < numero2:
  for i in range(numero1 + 1, numero2):
    print(i)
elif numero1 > numero2:
  for i in range(numero2 + 1, numero1):
    print(i)
else:
  print("Os números são iguais, não há intervalo entre eles.")