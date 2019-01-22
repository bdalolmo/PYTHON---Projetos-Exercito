# -*- coding: utf-8 -*- 

def  soma(num1,num2):
    print("A soma eh : ",(num1+num2))

soma(6,7)


lista=[6,9]
soma(*lista)


def soma2(*numeros):
    total=0
    for numero in numeros:
        total+=numero
    print("A soma do eh:", total)


lista2=[300,65,3,45,9,83,13]
soma2(*lista2)



