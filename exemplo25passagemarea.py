# -*- coding: utf-8 -*-
assentosVagos=[8,7,0,24,11,60]
quantidadedeRotas = len(assentosVagos)
for rota,assentosDisponiveis in enumerate(assentosVagos):
    print("Rota %d possui %d assentos vagos" % (rota+1,assentosDisponiveis))
while True:
    rotaEscolhida=int(raw_input("Escolha uma rota de 1 a %d(Digite 0 para sair)" % quantidadedeRotas))
    if rotaEscolhida == 0:
        print("sistema Finalizado.......tchau!!")
        break
    if rotaEscolhida > quantidadedeRotas or rotaEscolhida <1:
       print("Rota Inválida..")
    elif assentosVagos[rotaEscolhida-1]== 0:
        print("Rota com vagas indisponiveis")
    else:
        quantidadePassagens = int(raw_input("Quantas passagens deseja comprar? (%d assentos disponiveis)" % assentosVagos[rotaEscolhida-1]))  
        if quantidadePassagens > assentosVagos[rotaEscolhida-1]:
            print("Você escolheu uma quantidade de passagens maior do que o disponivel")
        elif quantidadePassagens < 1:
            print("Numero d passagens invalida - Escolha novamente ")
        else:
            assentosVagos[rotaEscolhida-1] -= quantidadePassagens
            print("Compra da(s) passagens finalizadas com sucesso ")
            for rota,assentosDisponiveis in enumerate(assentosVagos):
                print("Rota %d possui %d assentos vagos" % (rota+1,assentosDisponiveis))
 