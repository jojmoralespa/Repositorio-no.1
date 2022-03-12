
name = None
names ={}

while name != 'done':
    name = input("Enter names: ")
    if name == 'done':
        break
    elif not name in names:
        names[name] = 1
    else:
        names[name] += 1
x =names.get("johan",)
print(names)