dados = ['Breno','Dirce','Sete','Cachorro']
print(dados)
print("\n".join(dados))
print("-".join(dados))
print("************".join(dados))



palavra="breno geraldo dalolmo"
print("startswith=retorna verdadeiro se a string inicia com uma substring: ",palavra.startswith("breno"))
print("strip elimina espacos em branco a esquerda e direita: ", ".","   breno dalolmo    ".strip(),".")

print("zfill preenche a esquerda com zero(0)","465".zfill(8))
print("swapcase - inverte caracteres maisculos/minuscylos", "BrEno DaLoLmO".swapcase())