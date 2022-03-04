
sub_list = ["Matemáticas", "Física", "Química", "Historia" , "Lenguas"]
grades_list = []
count = 0

for subject in sub_list:
    grade = float(input(f"Qué nota sacó en {subject}: "))
    grades_list.append(grade)

print("\n Compendio de Notas: \n")
for subject in sub_list:
    print(f"en {subject} has sacado {grades_list[count]}")
    count +=1
