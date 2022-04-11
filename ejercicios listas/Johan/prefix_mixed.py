def is_leap(year):
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False

'''year = int(input())
print(is_leap(year))'''

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


list2 = list(map(lambda x: x*2 , list1 )) 
#map y funciones lambda mejor para todos los elementos

list3 = [ x*2 for x in list1 if x % 2 == 0]
#Comprensión de listas mejor para filtrar elementos

#print(list2,"\n",list3)

n = int(input())
string = ''
for i in range(1,n+1):
    string += str(i)

print(string)
