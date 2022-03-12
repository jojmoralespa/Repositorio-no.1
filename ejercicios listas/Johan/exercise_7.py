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

for i in range(len(list_copy)-1,-1,-1):
        if (i+1) % 3 ==0:
                list_copy.pop(i)

print(*list_copy, sep = " ")

lst =[1,2]
for v in range(2):
        lst.insert(-1,lst[v])

print(lst)
print(range(5))

del lst[:]
print(lst)

x = 2%1

print(x)

dtc = {}
dtc['1']=(1,2)
dtc['2']=(2,1)

for x in dtc.keys():
        print(dtc[x][1],end = "")

x = 'hello'
y = 'there'

print(x + y)
