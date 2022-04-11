

def suma(n):
    if n == 0:
        return 0
    return n + suma(n-1)

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

lis = list(range(1,6))

def printf(list,i):
    if i == len(list):
        return quit()     
    print(list[i])
    return printf(list,i+1)

def printf2(list,i):
    if i == 0:
        print(list[i])
        return quit()     
    print(list[i])
    return printf2(list,i-1)

def searching(list,n,i):
    if list[i] == n:
        return i
    else:
        return searching(list,n,i-1)

matrix = [[2,4],[3,4]]
def matrix_print(matrix,i,j):
    if i 

print(searching(lis,3,4))