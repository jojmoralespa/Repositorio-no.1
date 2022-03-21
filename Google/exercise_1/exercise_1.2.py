#Read txt

t = int(input())
element_list = list()

def reverse(i,j,list_aux):
    if j != len(list_aux)-1:
        list_1 = list_aux[:j+1]
        list_2 = list_aux[j+1:]
        count = i
        for n in range(len(list_1)-1,i-1,-1):
            list_aux[count] = list_1[n]
            count += 1
        for n in range(0,len(list_2)):
            list_aux[count] = list_2[n]
            count += 1
        return list_aux
    else:
        list_1 = list_aux.copy()
        count = i
        for n in range(len(list_1)-1,i-1,-1):
            list_aux[count] = list_1[n]
            count += 1
        return list_aux

def count(list):
    cost = 0
    for i in range(len(list)-1):
        j = list.index(min(list[i:]))
        if i == j:
            cost += j - i + 1
            continue
        else:
            list = reverse(i,j,list)
            cost += j - i + 1
    return cost


############

for n in range(1,t+1):
    num_list = int(input())
    list_case = input().split()
    for element in list_case:
        int_element = int(element)
        list_case[list_case.index(element)] = int_element
    value = count(list_case)

    print("Case #{}: {} ".format(n,value ))
