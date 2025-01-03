# Initialization of values
total_deduction = 0
gross_income = 0
net_income = 0
pagibig_cont = 100.00
employee_name = ""


# Input of variables
employee_name = str(input("Enter the employee's name:"))
employee_dep = str(input("Enter employee's department:"))
rate_hr = float(input("Enter the employee's rater per hour:"))
num_hrs_day = float(input("Enter the employee's number of working hours per day:"))
num_days_week = float(input("Enter the number of days per week:"))
num_weeks_month = int(input("Enter the number of weeks per month:"))



# Setting up the formula for the gross income.
gross_income = round(num_hrs_day * num_days_week * num_weeks_month * rate_hr)


# Determining the SSS contribution and Philhealth contribution.
if 0 <= gross_income <= 20000:
    sss_cont = 125.75
    philhealth_cont = 100.00
elif 20001 <= gross_income <= 50000:
    sss_cont = 2200.50
    philhealth_cont = 1200.00
elif 50001 <= gross_income <= 75000:
    sss_cont = 4800.00
    philhealth_cont = 6800.00
else:
    sss_cont = 5800.00
    philhealth_cont = 8800.00


# Setting up the formula for total deduction and net income
total_deduction = pagibig_cont + sss_cont + philhealth_cont
net_income = gross_income - total_deduction


# Displaying the calculated information
print(f"Employee Name: {employee_name}")
print(f"Employee department: {employee_dep}")
print(f"Net income: {net_income:.2f}")
print(f"Gross Income: {gross_income:.2f}")
print(f"Total deduction: {total_deduction}")
print(type(employee_name))