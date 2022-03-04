

sub_list = []
asignaturas = None
while  asignaturas != "done":
    #Data input
    asignaturas = input(" Enter subject ( if is done, write 'done' ): ")
    
    if asignaturas != "done":
        sub_list.append(asignaturas)

    #sub_list.append(asignaturas)

#sub_list.pop()
print(sub_list)