
#input data
print("the operations will be made in the same numbers order that you put in.")
str_number_1 = input("number 1:")
str_number_2 = input("number 2:")

try:
    #float numbers
    number_1 = float(str_number_1)
    number_2 = float(str_number_2)

    #operations
    sum = number_1 + number_2

    substraction = number_1 - number_2

    div = number_1 / number_2

    prod = number_1*number_2

    mod = number_1 % number_2

    #Results
    print("The results are shown below:")
    print(f"sum = {round(sum,2)}")
    print(f"substraction = {round(substraction,2)}")
    print(f"division = {round(div,2)}")
    print(f"Product = {round(prod,2)}")
    print(f"modulus = {round(mod,2)}")
except:
    print("Data error")
