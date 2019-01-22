# -*- coding: utf-8 -*- 
print("sem usar funcoes, a soma e ",(5+6))

def soma (num1,num2):
    print("Usando funcoes (DEF)",(num1+num2))

soma(5,6)

#usando comando return

def soma1 (num1,num2):
    return(num1+num2)

print("Usando funcoes (DEF) com return,a soma eh",soma1(8,7))


def numeropar(numero):
    return(numero % 2==0)
print("O numero 4 e par",numeropar(4))

def parouimpar(numero1):
    if numeropar(numero1):
         return "par"
    else:
        return "impar"

print("O numero 7 eh ",parouimpar(7))


def pesquisar(lista,codigo):
    for i, codigos in enumerate(lista):
       if codigos == codigo:
            return("Codigo %d encontrado no indice %d" % (codigo,i))
       return("O Codigo %d não foi encontrado" % codigo)

listaProdutos=[4,8,2,67,99,56,2,3]
print(pesquisar(listaProdutos,8))
print(pesquisar(listaProdutos,4))
print(pesquisar(listaProdutos,98))
print(pesquisar(listaProdutos,100))


dicionarioCursos={"java":150,
                "python":145,
                "pascal":80,
                "Android":180}

def pesquisaDicionario(dicionarioPesquisar,cursoPesquisar):
      if cursoPesquisar in dicionarioPesquisar:
           print("Curso localizado, o seu preço é R$ %5.2f" % dicionarioPesquisar[cursoPesquisar])
      else:
            print("Curso nao localizado!!")

pesquisaDicionario(dicionarioCursos,"java")
