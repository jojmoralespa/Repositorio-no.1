
sub_list = ["Mathematics","Physics","Chemistry","History","Language"]

grades_list = []
grades_copy =[]
for subject in sub_list:
    try:
        grade_str = input(f"Enter grade of {subject} :")
        grade = float(grade_str)
        grades_list.append(grade)
    except:
        print("isn't a number")

grades_copy = grades_list.copy()
for grade in grades_copy:
    if grade >= 3:
        ind = grades_list.index(grade)
        grades_list.pop(ind)
        sub_list.pop(ind)

print(grades_list)

print("\n Subject for repeat: \n")
for subject in sub_list:
    print(f"You must to repeat {subject}")


