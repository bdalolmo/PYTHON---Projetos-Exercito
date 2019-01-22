# -*- coding: utf-8 -*- 

listaNomes=["Breno","Dirce","Sete"]
print(listaNomes[1])

dicionarioNomes={1:"Breno",
                 2:"Dirce",
                 3:"Sete"}

print(dicionarioNomes.keys())
print(dicionarioNomes.values())
print(dicionarioNomes[1])



dicionarioCursos={"java":150,
                "python":145,
                "pascal":80,
                "Android":180}


##acrescentar elemento ao dicionario
dicionarioCursos["Excel"]=90

print("java" in dicionarioCursos)

#implementando pesquisa
while True:
    nomepesquisa = raw_input("Nome do curso a pesquisar: ")
    if nomepesquisa=="fim":
         break
    if nomepesquisa in dicionarioCursos:
        print("Curso localizado, o seu preço é R$ %5.2f" % dicionarioCursos[nomepesquisa])
    else:
        print("Curso nao localizado!!")