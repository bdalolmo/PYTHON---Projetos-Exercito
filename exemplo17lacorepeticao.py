for numeros in "123456789":
    print("Numero",numeros)
else:
    print("Fim")

for numeros in range(10):
    print("Numero.:",numeros)
    if numeros > 6:
        break


for nomes in ["Neri","Breno","Lucia","Dirce"]:
    print("Nomes",nomes)
else:
    print("Fim")


dadostupla = [("a","b"),("c","d"),("d","f")]
for (alf1, alf2) in dadostupla:
    print (alf1,alf2)

for numeros in range(20,30):
    if numeros == 25:
        continue
    print("Numero.: ",numeros)
else:
    print("Fim")




for tabuada in range(1,10):
    #print("7 * ",tabuada," = ",(7*tabuada))
    print("7 * %d = %d" % (tabuada,(7*tabuada)))

numtabuada = int(raw_input("Digite um numero para a tabuada.:"))
 for tabuada in range(1,10):
     print(" %d * %d = %d" % (numtabuada, tabuada(numtabuada*tabuada))) 



somatotal=0;
for soma in range(1,12):
    somatotal+=soma
    print("A Soma é %d" %somatotal)