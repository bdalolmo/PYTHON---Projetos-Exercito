notaAluno=int(input("Digite a nota do Aluno.:"))
mediaparapassar = 6
if notaAluno >= mediaparapassar:
    print("Aluno Aprovado")
elif notaAluno >= 4:
    print("Aluno Recuperacao")
else:
    print("Aluno Reprovado")
