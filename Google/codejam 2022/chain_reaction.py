
t = int(input())
def cases(n, point_index):
    index_list2 = list(set(point_index))
    index_tries = []
    for ind in range(1,n+1):
        if ind not in index_list2 and point_index[ind-1] != 0:
            index_tries.append(ind)
    return index_tries

def max_first(i,list_aux):
    list_1 = list_aux[:i+1]
    list_2 = list_aux[i+1:]
    lista_aux = list_2 + list_1
    return list_aux

def fun_calc(fun_values , point_index , n):
    
    for index in cases(n,point_index):
        fun = max_first(index-1,fun_values)
        point = max_first(index-1,point_index)
        case_list=[]
        while len(fun) != 0:
            list_way = []
            if point[len(point)-1]==0:
                list_way.append(fun[len(point)-1])
                fun.pop(len(point)-1)
                point.pop(len(point)-1)
            else:
                lista_usados =[]
                punto_llegada = None
                indice = len(point)-1
                while punto_llegada != 0:
                    list_way.append(fun[len(point-1)])
                    lista_usados.append(fun[len(point-1)])
                    fun.pop(len(point)-1)
                    point.pop(len(point)-1)

def recur(fun,point, fun_values, lista_usados, list_way):
    list_way.append(fun[len(point-1)])
    lista_usados.append(fun[len(point-1)])
    fun.pop(len(point)-1)
    point.pop(len(point)-1)

for i  in range (t):
    n = int(input())
    fun_values = list(map(int, input().split()))
    point_index = list(map(int, input().split()))
    #print(f"Case #{i+1}: {}")

print(cases(n,point_index))


def array_dict(n, funValue , pointIndex):
    dic = dict()
    for k in range(1,n+1):
        dic[str(k)]=[pointIndex[k-1],funValue[k-1]]
    
    return dic