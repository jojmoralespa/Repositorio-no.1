
t = int(input())

def ascii_art(r,c):
    f = 2*r + 1
    col = 2*c + 1
    for i in range(1,f+1):
        row = ''
        for j in range(1,col+1):
            if i <= 2 and j <= 2:
                row += '.'
            else:
                if i % 2 != 0:
                    if j % 2 != 0:
                        row += '+'
                    else:
                        row += '-'
                else:
                    if j % 2 != 0:
                        row += '|'
                    else:
                        row += '.'
        print(row)

for i  in range (t):
    rc = input().split()
    r = int(rc[0])
    c = int(rc[1])
    print(f"Case #{i+1}:")
    ascii_art(r,c)


