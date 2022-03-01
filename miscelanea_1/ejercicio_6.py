
#input data
hours_str = input("Enter Hours worked:")
hour_value_str = input("Enter Hour value: $ ") 

try:
    hours = float(hours_str)
    hour_value = float(hour_value_str)

    #Amount to pay
    pay = hours*hour_value
    print(f"You must to pay : $ {pay}")
except:
    print("Data error")