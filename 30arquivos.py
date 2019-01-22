# -*- coding: utf-8 -*- 
arquivo = open("familia.txt","w")
arquivo.write("Familia do Breno: \n\n")
arquivo.write("Breno\n")
arquivo.write("Dirce\n")
arquivo.write("Sete\n")
arquivo.close

arquivo=open("familia.txt","r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()