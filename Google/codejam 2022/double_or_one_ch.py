def order(arr):
    
    listAux =[]
    cont = 1
    i=0
    while( i < len(arr)-1):
        if(arr[i] < arr[i+1] ):
            listAux.append(arr[i]*2*cont)
            cont=1
            i+=1
        elif( arr[i] == arr[i+1]):
            j=i
            cont=1
            while(arr[j] == arr[j+1] ):
                cont+=1
                j+=1
                if(j == len(arr)-1):
                    break
            if(j == len(arr)-1):
                listAux.append(arr[i]*(cont-1))
                break
            i+=cont-1
        else:
            listAux.append(arr[i]*cont)
            cont=1
            i+=1
    listAux.append(arr[-1])
    return "".join(listAux)


t = int(input())

for i  in range (t):
    arr = list(input())
    print(f"Case #{i+1}: {order(arr)}")