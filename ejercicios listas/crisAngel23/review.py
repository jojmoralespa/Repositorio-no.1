
##Algorithms

from operator import le
from os import sep


try:
    number = int(input("Ingrese el número de la loteria: "))
except NameError:
    print("El dato ingresado no es un numero !")
except:
    print("Data error")

numberList = list(str(number))


for i in range(len(numberList)):
   numeroantes = int(numberList[i])
   for j in range(i+1,len(numberList)):
       numerodespues = int(numberList[j])
       if(numeroantes > numerodespues):
           numeroAux = str(numeroantes)
           numberList[i] = str(numerodespues)
           numeroantes = numerodespues
           numberList[j] = str(numeroAux)
        
print(*numberList)






