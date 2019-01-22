dados = ['Breno','Dirce','Sete','Cachorro']
print(dados)
print("\n".join(dados))
print("-".join(dados))
print("************".join(dados))


palavra="breno"
print(palavra.ljust(30),"casa")
print(palavra.rjust(30),"casa")
print("partition, divide a string em uma tupla com 3 elementos: ","brenogeraldodalolmo".partition("geraldo"))
print("rpartition, divide a string em uma tupla com 3 elementos: ","brenogeraldodalolmo".rpartition("geraldo"))
print("split -> divide a String em uma lista", "Breno;Geraldo;Dalolmo".split(";"))
print("rsplit -> divide a String em uma lista", "Breno Geraldo Dalolmo".rsplit())

