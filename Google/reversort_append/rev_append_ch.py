t = int(input())

def add_0(n,diff):
    n += '0'*diff
    return n

def sort_append(arr,n):
    count = 0
    for i in range(1,n):
        if int(arr[i-1])<int(arr[i]):
            continue
        else:
            diff = len(arr[i-1])-len(arr[i])
            if diff > 0 :
                arr[i] = add_0(arr[i],diff)
                count += diff
                rest = (int(arr[i-1]) - int(arr[i]))

                if(int(arr[i-1]) >= int(arr[i])):
                    if(len(str(rest+1))>(diff)):
                        arr[i] = add_0(arr[i],1)
                        count +=  1
                    else:
                        arr[i] = str(int(arr[i])+rest+1)                
            else:
                arr[i] = add_0(arr[i],1)
                count +=  1
    return count

for i  in range (t):
    n = int(input())
    arr = input().split()
    print(f"Case #{i+1}: {sort_append(arr,n)}")