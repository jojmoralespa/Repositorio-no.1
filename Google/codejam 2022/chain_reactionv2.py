
handle = open('D:\\Users\\Johan\\Desktop\\Proyecto\\Google\\codejam 2022\\ts2_input.txt')

def resursiva (dic, init, setAux, listMax):
    
    init = str(init)

    if init in setAux or init == "0":
        return max(listMax)

    setAux.add(init)
    listMax.append(dic[init][1])

    return resursiva(dic,dic[init][0], setAux, listMax)  

def calcularValue ( listaSet, dic):
    
    listAux =[]
    setAux = set()
    for modulo in listaSet:
        listMax=[]
        listAux.append(resursiva(dic,modulo, setAux, listMax))
    
    return sum(listAux)

def cases(n, point_index):
    index_list2 = list(set(point_index))
    index_tries = []
    for ind in range(1,n+1):
        if ind not in index_list2:
            index_tries.append(ind)
    return index_tries


def array_dict(n, funValue , pointIndex):
    dic = dict()
    for k in range(1,n+1):
        dic[str(k)]=[pointIndex[k-1],funValue[k-1]]
    
    return dic


element_list = list()

for line in handle:
    line = line.rstrip()
    element_list.append(line)

t = int(element_list[0])

count = 1
list_out = []
for h in range(1,t+1):

    n = int(element_list[count])
    funValue = list(map(int, element_list[count+1].split()))
    pointIndex = list(map(int, element_list[count+2].split()))
    count += 3
    listaAux = cases(n,pointIndex)
    listaAux = list(map(str, listaAux))


    listGlobal=[]
    for i in range(len(listaAux)):
        listGlobal.append(calcularValue(listaAux[i:]+listaAux[:i],array_dict(n,funValue,pointIndex)))
    
    #list_out.append("Case #{}: {}".format(h,max(listGlobal)))
   
    print("Case #{}: {}".format(h,max(listGlobal)))
'''
handle2 = open('D:\\Users\\Johan\\Desktop\\Proyecto\\Google\\codejam 2022\\ts1_output.txt')
element_list2 = []

for line in handle2:
    line = line.rstrip()
    element_list2.append(line)

|
'''