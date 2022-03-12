
from operator import itemgetter


name_l = open('D:\\Users\\Johan\\Desktop\\Proyecto\\dictionaries_exercises\\names.txt')
names_d = {}

for line in name_l:
    line.rstrip()
    words = line.split()
    for name in words:
        names_d[name] = names_d.get(name,0) + 1

lista_nombres = list()
lista_ejercicio = names_d.items()
for k,v in names_d.items():
    n_tuple = (v,k)
    lista_nombres.append(n_tuple)
    
#print(lista_nombres)
lista_sorted = sorted(lista_nombres, reverse = True)
x = sorted(lista_ejercicio,key = lambda count: count[1] ,reverse = True)
print(x)
for v,k in lista_sorted[:1]:
    print(k,v)

