# -*- coding: utf-8 -*-
nome = raw_input("Digite seu nome.:")
print('primeiro caracter em maisculo ', nome.capitalize())
print('centraliza',nome.center(30))
print('quantas letras E tem no nome:',nome.count("e"))
print('Retorna true se o nome terminar com ....',nome.endswith("fante") )
print('Find retorna posicao de String :',nome.find("e"))
print('Index retorna posicao da primeira ocorrencia ',nome.index("e",2))