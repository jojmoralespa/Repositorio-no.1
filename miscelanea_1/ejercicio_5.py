
print(" Triangle Area:")

#input data
base_str = input("Enter width:")
heigth_str = input("Enter heigth:")     

try:
    base = float(base_str)
    heigth = float(heigth_str)
    
#Area of rectangle
    area = base*heigth/2
    print("The results are shown below:")
    print(f"Area = {area} u^2")

except:
    print("Data error")