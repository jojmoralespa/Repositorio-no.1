
#n = int(input("length (N) = "))
#c = int(input("Cost (C) = "))
n = 18
c = 39
c-= n - 1

list_nums = list(range(1,n+1))

def reverse(i,j,list_aux):
    list_1 = list_aux[i:j+1]
    count = i
    for n in range(len(list_1)-1,-1,-1):
        list_aux[count] = list_1[n]
        count += 1
    return list_aux
    
for i in range(n-2,-1,-1):
    if c != 0:
        j = list_nums.index(max(list_nums[i:]))
        list_nums = reverse(i,j,list_nums)
        c -= j - i
    else:
        break

print(list_nums)
