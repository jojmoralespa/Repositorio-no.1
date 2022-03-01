
#input data
pay_list = []
hour_list = []

count = 1
total_pay = 0
total_h = 0

try:
    while count <= 3:
        hours_str = input(f"Enter Hours worked in day {count}: ")
        hour_value_str = input(f"Enter Hour value in day {count}: $ ")

        hours = float(hours_str)
        hour_value = float(hour_value_str)
        hour_list.append(hours)

        #Amount to pay
        pay = hours*hour_value
        pay_list.append(pay)
        count = count + 1
    for value in pay_list:
        total_pay = total_pay + value
    #Total hours worked    
    for value in hour_list:
        total_h = total_h + value

    #Results
    print("")
    print("Results: ")
    print("")
    print(f"You must to pay : $ {round(total_pay,2)}")
    print(f"Total hours worked : {round(total_h,2)} h")

    # amount to pay each day
    count = 1
    for value in pay_list:
        print(f"amount to pay in day {count}: $ {round(value,2)}")
        count += 1

except:
    print("Data error")