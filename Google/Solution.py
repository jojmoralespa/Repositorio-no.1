def solv(S):
    if len(S)==1:
        return S
    first=[]
    for j in range(1,len(S)):
        if S[j-1] < S[j]:
            first.append(j-1)
    #print(first)
    if len(first)==0:
        return S
    left=[]
    for f in first:
        if f==0:
            left.append(0)
            continue
        l=f
        while l>0:
            if S[l-1]==S[f]:
                l-=1
            else:
                left.append(l)
                break
        if l==0:
            left.append(0)
    #print(left,first)
    res=''
    res=S[:left[0]]+S[left[0]:first[0]+1]+S[left[0]:first[0]+1]
    for j in range(1,len(first)):
        res+=S[first[j-1]+1:left[j]]+''+S[left[j]:first[j]+1]+''+S[left[j]:first[j]+1]+''
    res+=S[first[-1]+1:]
    return res
    #return S[:left]+S[left:first+1]+S[left:first+1]+S[first+1:]

t = int(input()) 
for i in range(1, t+1):
    S = input() 
    print(f"Case #{i}: {solv(S)}")
