# Initialization of values....
Net_income = 0
Gross_income = 0
total_deduction = 0
employee_name = ""
pag_ibig_contribution = 100.00

# Inputting the values of the variables
employee_name = str(input("enter employee's name"))
rate_per_hour = float(input("enter employee's rate per hour:"))
number_hours_per_day = float(input("enter employee's number of working hours per day"))
numbers_days_per_week = int(input("enter employee's number of days per week"))
numbers_weeks_per_month = int(input("enter employee's number of weeks per month"))
SSS_contribution = float(input("enter employee's SSS contribution"))
philhealth_contribution = float(input("Enter employee's philhealth contribution"))
tax_contribution = float(input("enter employee's tax contribution"))

# setting the formula for the gross income, total deduction, and net income
gross_income = rate_per_hour * number_hours_per_day * numbers_days_per_week * numbers_weeks_per_month
total_deduction = SSS_contribution + philhealth_contribution + tax_contribution + pag_ibig_contribution
net_income = gross_income - total_deduction

# displaying for the computed value of gross income, total deduction, and net income
print(" employee Name:", employee_name)
print("net income", net_income)
print("gross income", gross_income)
print("total deduction", total_deduction)
