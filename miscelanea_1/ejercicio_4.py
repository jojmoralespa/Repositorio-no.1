
print(" Rectangle Area:")

#input data
width_str = input("Enter width:")
heigth_str = input("Enter heigth:")     

try:
    width = float(width_str)
    heigth = float(heigth_str)

#Area of rectangle
    area = width*heigth
    print("The results are shown below:")
    print(f"Area = {area} u^2")

except:
    print("Data error")