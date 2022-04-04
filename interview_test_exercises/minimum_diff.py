
list = [3,8,30,2,20,10,5,15,21,31]

def min_diff(list):    
    list = sorted(list)
    print(list)
    list_min = []
    list_dif = []

    for i in range(1,len(list)):
        diff = list[i] - list[i-1]
        list_dif.append(diff)

    min_dif = min(list_dif)
    print(f'minimum difference = {min_dif}')

    for i in range(len(list_dif)):
        if list_dif[i] == min_dif:
            list_min.append(list[i:i+2])

    for element in list_min:
        print(element)

min_diff(list)