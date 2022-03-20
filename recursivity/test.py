
list = list()
element = None

while element != 'done':
    element = input("Enter data: ")
    if element == 'done':
        break
    else:
        list.append(int(element))

sum = int(input("enter result of sum: "))

for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[i] + list[j] == sum and i != j:
            print(f'las posiciones {i} y {j} de la lista dan como resultado {sum}.')
            break
    break

