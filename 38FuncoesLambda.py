# -*- coding: utf-8 -*- 

def  soma(num1,num2):
    print("A soma eh : ",(num1+num2))

soma(6,7)


somarLambda = lambda num1,num2: num1+num2
print("A soma lambda eh ", somarLambda(6,7))



multiplicarLambda = lambda num1,num2: num1*num2
print("A mult lambda eh ", multiplicarLambda(6,7))


multiplicar = lambda num1: num1*6
print("A mult lambda eh ", multiplicar(6))