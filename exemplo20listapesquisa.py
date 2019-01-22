# -*- coding: utf-8 -*-
listanomes = ["Breno","Dirce","Sete","Dani"]
print(listanomes)
nomepesquisar=raw_input("Digite o nome a ser pesquisado.: ")
encontrou=False
numalunos=0
while numalunos < len(listanomes):
    if nomepesquisar== listanomes[numalunos]:
        encontrou=True
        break
    numalunos+=1
if encontrou == True:
    print("Aluno localizado e matriculado")
else:
    print("Aluno nao localizado")




print("######################################")


for alunos in listanomes:
    if nomepesquisar==alunos:
        print("Aluno localizado e matriculado")
        break
    else:
        print("Aluno nao localizado")

print("######################################") #com problemas
 
temperaturas=[40,33,-3,2,9,6,20]
maior=temperaturas[0]
for listatemperaturas in temperaturas:
    if listatemperaturas > maior:
        maior=listatemperaturas
print('Com laço for a maior temperatura registrada.: ',maior)

menor=temperaturas[0]
for listatemperaturas in temperaturas:
    if listatemperaturas < menor:
        menor=listatemperaturas
print("Com laço FOR A menor temperatura registrada",menor)

i=0
while i< len(temperaturas):
    if temperaturas[i] > maior:
        maior=temperaturas[i]
    i+=1
print('Com laço While a maior temperatura registrada.: ',maior)
