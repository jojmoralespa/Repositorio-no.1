
array = ['Martin','Pedro','Maria','Martina','Mariana','Mongo']

prefix = ['Mart','Mar','Mong']

def pref_consulting(array,prefix):
    occurrences = []
    dict_occ = dict()
    for pref in prefix:
        count = 0
        for name in array:
            if len(name) > len(pref) and name.startswith(pref):
                count += 1
        occurrences.append(count)
    print(occurrences)

    for i in range(len(prefix)):
        dict_occ[prefix[i]] = occurrences[i]
    for k,v in dict_occ.items():
        print(f'\'{k}\' occurrences =',v) 

print(array)
print(prefix)

pref_consulting(array,prefix)
