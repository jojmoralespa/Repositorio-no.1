#Read txt

handle = open("sample_ts1_input.txt")
element_list = list()

for line in handle:
    line.rstrip()
    list_line = line.split()
    element_list.append(list_line)

for element in element_list:
    for i  in element:
        int_element = int(i)
        element[element.index(i)] = int_element

def reverse(i,j,list_aux):
    if j != len(list_aux)-1:
        list_1 = list_aux[:j+1]
        count = i
        for n in range(len(list_1)-1,i-1,-1):
            list_aux[count] = list_1[n]
            count += 1
        return list_aux
    else:
        list_1 = list_aux.copy()
        count = i
        for n in range(len(list_1)-1,i-1,-1):
            list_aux[count] = list_1[n]
            count += 1
        return list_aux

for list_index in range(1,len(element_list)):
    if list_index % 2 != 0:
        continue
    else:
        list = element_list[list_index]
        lista_aux = list
        cost = 0
        for i in range(len(list)-1):
            j = list.index(min(list[i:]))
            if i == j:
                cost += j - i + 1
                continue
            else:
                list = reverse(i,j,lista_aux)
                cost += j - i + 1

    print(f'Case #{int(list_index/2)}:',cost)

