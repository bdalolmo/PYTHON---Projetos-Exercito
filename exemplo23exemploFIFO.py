# -*- coding: utf-8 -*-

print("--------------FIFO----------------")
passageiros = ["Breno","Dirce","Sete","Dani","Renata","Vitoria"]
posicaoultimo=len(passageiros)

while True:
    print("Tem %d passageiros na fila" % posicaoultimo)
    print("Os passageiros na fila sao :")
    for i, num in enumerate(passageiros):
        print("Passageiro.: [%d]--> %s" % (i+1,num))
    print("Digite 1 para add uma pessoa na fila")
    print("Digite 2 para dizer que pessoa foi atendida (saiu da fila)")
    print("Digite 3 para sair")
    acao = int(raw_input("Informe a operacao (1 ou 2 ou 3)"))
    if acao == 1:
        pessoa=raw_input("Digite o nome da pessoa que entrou na fila...")
        passageiros.append(pessoa)
        posicaoultimo+=1
    elif acao==2:
        if (len(passageiros))>0:
            passageiros.pop(0)
            posicaoultimo-=1
        else:
            print("A fila esta vazia")
    elif acao==3:
        print("FIM----------------------------------------------------")
        break        



 