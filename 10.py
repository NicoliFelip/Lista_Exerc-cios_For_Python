#10. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
#valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.
faturamentoB= 5400
faturamentoA=0
print(f"faturamento loja b: {faturamentoB}")
for i in range(1,6):
    clientes= int(input(f"Para cadastrar o cliente {i}, insira a soma do valor de todas as compras do mês que ele gerou:  "))
    faturamentoA+=clientes
print(f"o faturamento da loja A foi de: {faturamentoA}")
if faturamentoA >=faturamentoB:
    print ("faturamento da loja A foi menor que o da loja B")
    for a in range(faturamentoA,faturamentoB):
        print(f"com uma diferença de {a}")
else:
    print ("faturamento da loja A foi maior que o da loja B")
    for b in range(faturamentoB,faturamentoA):
        print(f"com uma diferença de {b}")