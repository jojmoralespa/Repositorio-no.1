#Data input

monthly_str = input("enter monthly salary (in USD): $ ")
usd_to_euro = 0.899523
usd_to_cop = 3883.004883

try:
    monthly = float(monthly_str)
    salary_15 = round(monthly/2,2)
    salary_w = round(monthly/4,2)
    salary_d = round(monthly/30,2)
    salary_h = round(salary_d/8,2)
    salary_m = round(salary_h/60,2)
    salary_s = round(salary_m/60 ,2)
    salary_usd_eur = round(monthly*usd_to_euro,2)
    salary_usd_cop = round(monthly*usd_to_cop,2)

    print(f"Fortnightly salary (USD): $ {salary_15:,}")
    print(f"Weekly salary (USD): $ {salary_w:,}")
    print(f"Salary per day (USD): $ {salary_d:,}")
    print(f"Salary per hour (USD): $ {salary_h:,}")
    print(f"Salary per minute (USD): $ {salary_m:,}")
    print(f"Monthly salary (USD) to (EUR): $ {salary_usd_eur:,}")
    print(f"Monthly salary (USD) to (COP): $ {salary_usd_cop:,}")
except:
    print("Data error")