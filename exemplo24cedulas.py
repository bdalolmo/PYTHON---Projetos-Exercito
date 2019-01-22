# -*- coding: utf-8 -*-
valor=float(raw_input("Digite o valor: "))
cedulas=0
valorcedulaatual=100
valoraserentregue=valor
cedulaoumoeda="cedula(s)"
while True:
    if valorcedulaatual<=valoraserentregue:
        cedulas+=1
        valoraserentregue-=valorcedulaatual
    else:
        print("valor a ser entregue",valoraserentregue)
        if cedulas >0:
            print("%d %s de R$ %5.2f" % (cedulas,cedulaoumoeda, valorcedulaatual))
        if valoraserentregue == 0:
            break
        if valorcedulaatual == 100:
            valorcedulaatual = 50
        elif valorcedulaatual==50:
            valorcedulaatual=20
        elif valorcedulaatual==20:
            valorcedulaatual=10
        elif valorcedulaatual==10:
            valorcedulaatual=5
        elif valorcedulaatual==5:
            valorcedulaatual=2
        elif valorcedulaatual==2:
            cedulaoumoeda="moeda(s)"
            valorcedulaatual=1
        elif valorcedulaatual==1:
            cedulaoumoeda="moeda(s)"
            valorcedulaatual=0.50
        elif valorcedulaatual==0.50:
            cedulaoumoeda="moeda(s)"
            valorcedulaatual=0.25
        elif valorcedulaatual==0.25:
            cedulaoumoeda="moeda(s)"
            valorcedulaatual=0.10
        elif valorcedulaatual==0.10:
            cedulaoumoeda="moeda(s)"
            valorcedulaatual=0.05
        elif valorcedulaatual==0.05:
            cedulaoumoeda="moeda(s)"
            valorcedulaatual=0.01
            ("uma moeda de 1 centavo")
            break
        cedulas=0