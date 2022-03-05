
ganadores =[]
ganadores_ordenados = []
entrada = None

while entrada != "done":
    try:
        entrada = input("introduzca los numeros ganadores: ")
        entrada_int = int(entrada)
        ganadores.append(entrada_int)
    except NameError:
        print("no es un numero")
    except:
        print("Data error")
        break
        
ganadores_p = ganadores

min = None

while len(ganadores_p) != 0:
    for value in ganadores_p:
        if min == None:
            min = value
        if min >= value:
            min = value
    ganadores_ordenados.append(min)
    ganadores_p.remove(min)
    min = None

print(ganadores_ordenados)
