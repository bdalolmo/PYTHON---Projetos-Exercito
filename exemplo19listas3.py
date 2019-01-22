# -*- coding: utf-8 -*-
listanomes = ["Breno","Dirce","Sete","Dani"]
print(listanomes)
listanomes.reverse()
print(listanomes)


for nomeslista in listanomes:
    print(nomeslista)

listanomes.sort()
print(listanomes)

for i,nomeslista in enumerate (listanomes):
    print("Lista de nomes.:",i+1,"-->",nomeslista)

listafamilia=[]
while True:
    pessoafamilia=raw_input("Digite uma pessoa de sua familia(0 se acabou)")
    if pessoafamilia =="0":
        break
    listafamilia.append(pessoafamilia)
for a in listafamilia:
    print(a)

