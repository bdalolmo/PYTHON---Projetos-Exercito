# -*- coding: utf-8 -*- 

dicionarioCursos={"java":[150, "basico","desktop"],
                "python":[145, "intermediario","desktop e web"],
                "pascal":[80, "avancado","desktop"],
                "Android":[180,"basico","robotica"]}

print("Dados de java (usndo get).:",dicionarioCursos.get("java"))
print("Dados de java (usando setdefault).:",dicionarioCursos.setdefault("java"))


for chave,informacoes in dicionarioCursos.items():
    print("Dicionario .: ",chave)
    print("valor .: %5.2f" % informacoes[0])
    print("Nivel .: ",informacoes[1])
    print("Observacao .: ",informacoes[2])


copiaDicionariodeCursos = dicionarioCursos
print("copiaDicionariodeCursos=",copiaDicionariodeCursos)

copia2DicionariodeCursos = dicionarioCursos.copy
print("copia2DicionariodeCursos=",copia2DicionariodeCursos) # outra maneira de copiar



print(dicionarioCursos)
dicionarioCursos.clear()
print("Depois de clear.: ",dicionarioCursos)

