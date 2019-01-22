# -*- coding: utf-8 -*-
enome="Breno"
sobrenome="Dalolmo"

nomecompleto=nome+" "+sobrenome

print(nomecompleto)


print("---------------String Fatiamaento-------------------")

print(nome[0:4])



('----------composição-----------')

breno = 'sdfsdfsd'

nome=raw_input("Digite seu nome: ")
print nome
idade=int(raw_input("Digite a idade: "))
salario=float(input("Digite o salario: "))
print("Nome.:",nome, " - idade",idade, " - salario ",salario )
print("Nome.: %s - idade %d - salario %d" % (nome,idade,salario )) 