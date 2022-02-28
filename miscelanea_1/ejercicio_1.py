import math

pi = math.pi

#input data
radius_str = input("enter radius: ")

try:
    radius = float(radius_str)
    #Area function
    def area_function (r):
        area = round(pi*(r**2),2)
        return area

    #Perimeter function
    def perimeter_function (r):
        perimeter = round(2*pi*r,2)
        return perimeter

    #Volume function
    def volume_function (r):
        volume = round((4/3)*pi*(r**3),2)
        return volume

    #Results
    print("The results are shown below:")
    print(f"Area: {area_function(radius)} u^2")
    print(f"Perimeter: {perimeter_function(radius)} u")
    print(f"Volume: {volume_function(radius)} u^3")

except:
    print("Data error")
