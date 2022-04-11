import sys
sys.setrecursionlimit(10**6)

def recsolv(graphin,root,F):
    if root not in graphin:
        return [F[root-1],F[root-1]]
    cursum=0
    curflow=0
    for node in graphin[root]:
        tmp=recsolv(graphin,node,F)
        if cursum == 0:
            cursum+=tmp[0]
            curflow=tmp[1]
        else:
            if tmp[1] < curflow:
                cursum+=tmp[0]
                curflow=tmp[1]
            else:
                cursum+=tmp[0]
    if root == 0:
        return cursum
    if curflow <= F[root-1]:
        cursum+=F[root-1]-curflow
        curflow=F[root-1]
        return cursum,curflow
    return cursum,curflow

def solv(F,P,N):
    graphin={}
    for j in range(N):
        try:
            graphin[P[j]].add(j+1)
        except:
            graphin[P[j]]=set([j+1])
    return recsolv(graphin,0,F)

t = int(input()) 
for i in range(1, t+1):
    N = int(input()) 
    F = [int(s) for s in input().split(' ')]
    P = [int(s) for s in input().split(' ')]
    print(f"Case #{i}: {solv(F,P,N)}")
