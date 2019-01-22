# -*- coding: utf-8 -*-
numeros=[40,33,-3,2,9,6,23,61,30]
for num in numeros:
    if num % 2==0:
        print("O numero ",num," e par")
    else:
        print("O numero ",num," e impar")

numeros=[40,33,-3,2,9,6,23,61,30]
for num in numeros:
    if num % 2==0:
        print("O numero ",num," e par")
    else:
        print("O numero ",num," e impar")

i=0
while i< len(numeros):
    if numeros[i] % 2 ==0:
        print("O numero ",numeros[i]," e par")
    else:
        print("O numero ",numeros[i]," e impar")
    i+=1


##add para listas
pares=[]
impares=[]

for num in numeros:
    if num % 2==0:
        pares.append(num)
    else:
        impares.append(num)
    
print("os pares sao.: ",pares)
print("os pares sao.: ",impares)



