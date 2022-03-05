from io import open
from os import sep

archivo = None
nombreArchivo = 'C:\\Users\\crist\\OneDrive\\Desktop\\Project_Mogollan\\Repo_Ejercicios\\Repositorio-no.1\\ejercicios listas\\crisAngel23\\data.txt'

try:
    archivo = open(nombreArchivo, 'r')
except:
    print("error al leer el fichero.txt")

lineas = archivo.readlines()

abcList =list(lineas[0])

listAux = []

for i in range(len(abcList)):
    if (i+1) % 3 == 0:
        listAux.append(abcList[i])

for letter in listAux:
    abcList.remove(letter)

print("la lista resultante es: ")
print(*abcList)


