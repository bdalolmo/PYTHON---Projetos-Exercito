# -*- coding: utf-8 -*- 


def imprimeNome():
    global nome
    #print(nome)
    nome="Breno"
    print(nome)


nome="Videoaulas"
imprimeNome()

def somaLista(lista):
    global soma #problema
    for numLista in lista:
        soma += numLista
    return soma
soma=0
print(somaLista([5,7,6,8,9]))

