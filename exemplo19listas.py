# -*- coding: utf-8 -*-
alfabeto = ["a","b","c","d"]
print(alfabeto)

alfabeto += "efghij"
print(alfabeto)

alfabeto.extend("lmnopqrstuvxz")
print(alfabeto)


alfabeto += ["efghij"]# insere toda palavra

nomes = ["Breno","Dirce"]
print(nomes)

nomes.append("Sete")
print(nomes)

nomes.insert(0,"Dani")
print(nomes)


#removendo

alfabeto = ["a","b","c","d","e"]
print(alfabeto)

alfabeto.pop()
print(alfabeto)

del alfabeto[0]
print(alfabeto)

alfabeto.remove("b")
print(alfabeto)


##---------------##

print("----------------------COPIAA---------------------------------------------------------")

nomes = ["Breno","Dirce","Sete","Dani"]
print("lista de nomes.:", nomes)
nomes1=nomes 
print(nomes1 )
