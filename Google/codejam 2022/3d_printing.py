t = int(input())

def int_nums(list):
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

def print_3d(print1,print2,print3):
    ink_min = 0
    min_list = list()
    million = 1000000
    for i in range(4):
        minimum_i_list = (print1[i],print2[i],print3[i])
        min_i = min(minimum_i_list)
        ink_min += min_i
        min_list.append(min_i)
    if ink_min < million:
        print('IMPOSSIBLE')
    elif ink_min == million:
        print(*min_list, sep = ' ')
    else:
        ink_values = list()
        for i  in range(4):
            new_value = (min_list[i]*million)//ink_min
            ink_values.append(new_value)
        rest = million - sum(ink_values)
        ink_values[ink_values.index(max(ink_values))] += rest
        print(*ink_values, sep = ' ')
        
for i  in range (t):
    print1 = int_nums(input().split())
    print2 = int_nums(input().split())
    print3 = int_nums(input().split())

    print(f"Case #{i+1}: ", end= ""),
    print_3d(print1,print2,print3)
    
