t = int(input())


def length_array(list_s,n):
    list_sort = sorted(list_s)
    array = []
    for i in range(n):
        if len(array) < list_sort[i]:
            array.append(len(array)+1)
    return len(array)

for i  in range (t):
    n = int(input())
    dices = list(map(int, input().split()))
    length = length_array(dices,n)
    print(f"Case #{i+1}: {length}")