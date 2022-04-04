import math
from os import sep

def getNumber(listAux, num):
## to left : num = 0 , to right : num = 1
    count = 0
    if num == 0:
        for i in range(len(listAux)-2,-1,-1):
            if listAux[i] == 1:
               break
            count+=1
    else:
        for i in range(1,len(listAux)):
            if(listAux[i] == 1):
               break
            count+=1

    return count  

t = int(input())

for i in range(1,t+1):

    linea = input().split()
    n = int(linea[0])
    k = int(linea[1])

    numBath = []

    for i in range(n+2):

        if(i==0 or i ==n+1):
            numBath.append(1)
            continue

        numBath.append(0)

    numope = 0
    deno = 1
    
    if n % 2 != 0:
        for i in range(1,k+1):

                ## calcular indice de numBath donde ocupara el bath la persona
                ##case odd
                index = None
                
                if numope == 0:
                    deno*=2
                    numerador = n
                    numope = deno/2

                index = math.ceil( numerador/deno)
                numBath[index] = 1

                numerador+=2*n
                numope-=1
        ls = getNumber(numBath[:index+1],0)
        rs = getNumber(numBath[index:],1)
    else:
        for i in range(1,k+1):

                ## calcular indice de numBath donde ocupara el bath la persona
                ##case odd
                index = None
                if numope == 0:
                    deno*=2
                    numerador = n
                    numope = deno/2
                    index = math.ceil( numerador/deno)
                    numBath[index] = 1

                    numerador+=2*n
                    numope-=1 
                elif numope < deno/2:
                    index = math.ceil( numerador/deno)
                    numBath[index] = 1

                    numerador+=2*n
                    numope-=1     
                else: 
                    index = math.ceil((deno-1)*n/deno)
                    numope-=1
        ls = getNumber(numBath[:index+1],0)
        rs = getNumber(numBath[index:],1)

    print("Case #{}: {} {}".format(i,max(ls,rs),min(ls,rs)), sep=" ")


print(index)
print(numBath)
