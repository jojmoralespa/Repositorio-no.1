
#input data
pay_list = []

i = 1
total = 0
try:
    while i <= 3:
        hours_str = input(f"Enter Hours worked in day {i}: ")
        hour_value_str = input(f"Enter Hour value in day {i}: $ ")

        hours = float(hours_str)
        hour_value = float(hour_value_str)

        #Amount to pay
        pay = hours*hour_value
        pay_list.append(pay)
        i = i + 1
    for value in pay_list:
        total = total + value

    print(f"You must to pay : $ {round(total,2)}")
except:
    print("Data error")