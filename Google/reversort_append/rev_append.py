
t = int(input())

def add_0(n,diff):
    n += '0'*diff
    return n

def sort_append(arr,n):
    count = 0
    for i in range(1,n):
        if int(arr[i-1])<int(arr[i]):
            continue
        elif int(arr[i-1])==int(arr[i]):
            arr[i] = add_0(arr[i],1)
            count += 1
        else:
            diff = len(arr[i-1])-len(arr[i])
            if diff >= 0 and int(arr[i-1][0]) < int(arr[i][0]):
                arr[i] = add_0(arr[i],diff)
                count += diff
            elif diff >= 0 and int(arr[i-1][0]) == int(arr[i][0]):
                rest = (int(arr[i-1]) - int(arr[i]))
                if rest in range(9):
                    rest +=1
                    new_element = str(int(arr[i])+rest)
                    arr[i] = new_element
                    count += diff
                else:
                    arr[i] = add_0(arr[i],1)
                    count += diff + 1       
            elif diff >= 0 and int(arr[i-1][0]) > int(arr[i][0]):
                arr[i] = add_0(arr[i],diff+1)
                count += diff + 1
    return count

for i  in range (t):
    n = int(input())
    arr = input().split()
    print(f"Case #{i+1}: {sort_append(arr,n)}")
    
