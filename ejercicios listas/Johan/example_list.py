nombres = ["Mogollan" , "chayanne es gay" ,"Johan","Javier", "HOLA" , "6"]

for x in nombres:
    print(x)

r = range(2 ,len(nombres), 2 )

for iterador in r:
    print(nombres[iterador])


print(*nombres[:3],sep="")

entrada = input("Enter name: ")

print(entrada.replace("*"," "))
