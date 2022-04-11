
first = list(map(int, input().split()))

athletes = [list(map(int,input().split())) for i in range(first[0])]

'''for i in range(first[0]):
    atl = list(map(int, input().split()))
    athletes.append(atl)'''

k = int(input())

athletes.sort(key = lambda x: x[k])

for athlete in athletes:
    print(*athlete , sep = ' ')


