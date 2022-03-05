from io import open

archivo = open("D:\\Users\\Johan\\Desktop\\Proyecto\\ejercicios listas\\Johan\\lphabet.txt", 'r')

lineas = archivo.readlines()

list_alphabet =list(lineas[0])

list_copy = list_alphabet.copy()

for letter in list_copy:
     if (list_copy.index(letter)+1)%3 == 0:
        ind = list_alphabet.index(letter)
        list_alphabet.pop(ind)

print(*list_alphabet, sep = " ")

