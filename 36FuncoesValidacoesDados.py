# -*- coding: utf-8 -*- 


#semfuncao

while True:
    nota=int(raw_input("Digite a nota do aluno entre 0 e 10: "))
    if nota < 0 or nota > 10:
        print("Atencao, a nota %d eh invalida, tem que ser entre 0 e 10")
    else:
        print("Nota Valida")
        break

#com funcao
def validar(pergunta, notaMin, notaMax):
    while True:
        nota=int(raw_input(pergunta))
        if nota < notaMin or nota > notaMax:
            print("Atenção, a nota %d eh invalida, tem que ser entre %d e %d" %(nota,notaMin, notaMax))
        else:
            print("Nota Valida")
            return True

validar("Digite a nota do aluno.: ",2,8)
