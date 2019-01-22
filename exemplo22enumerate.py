# -*- coding: utf-8 -*-
numeros=[40,33,-3,2,9,6,23,61,30]
print(numeros)

i=0
for num in numeros:
    print("sem enumerate.: [%d] --> %d" %(i,num))
    i+=1


i=0
while i < len(numeros):
    print("WHILE sem enumerate.: [%d] --> %d" %(i,numeros[i]))
    i+=1


for i, num in enumerate(numeros):
    print("COM enumerate.: [%d] --> %d" %(i,num))
    

##FIFO

print("--------------FIFO----------------")

