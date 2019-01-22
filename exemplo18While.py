num=1

while num <= 10:

    print("numero.:",num)
    num=num+1 
else:
    print("Fim while")


nomes = ["Breno","Sete","Dirce","Joaozinho"]
indice=0
 
while indice < len(nomes): 
   print("Nomes.: ",nomes[indice])
   indice += 1
else:
    print("Fim dos nomes laco While")





numtabuada = int(raw_input("Digite um numero para a tabuada.:"))
for tabuada in range(1,10):
    print("%d * %d = %d" % (numtabuada, tabuada,(numtabuada*tabuada))) 
print("Fim tabuada FOR")
 
indice=1
while indice <=9:
     print("%d * %d = %d" % (numtabuada, tabuada,(numtabuada*tabuada))) 
     indice +=1
print("Fim tabuada WHILE")

