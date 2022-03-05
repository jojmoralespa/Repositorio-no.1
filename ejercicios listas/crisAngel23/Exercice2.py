
from msilib.schema import Error


subjects = ["Math","Physics","Chemestry","History","Language"]

subjectsRepeat=[]
grades = []


for course in subjects:
    try:
        grade = float(input(f"Put the grade for {course} course : "))
        grades.append(grade)
    except:
        print("Error")

for i in range(len(subjects)):
    if(grades[i] >= 3.0):
        subjectsRepeat.append(subjects[i])

for course in subjectsRepeat:
    grades.pop(subjects.index(course))
    subjects.pop(subjects.index(course))
    

print(f"the subjects you have to repeat are: ", end="")
print(*subjects, sep=" ")

