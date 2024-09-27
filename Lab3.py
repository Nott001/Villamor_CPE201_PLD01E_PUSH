# Initializing values
gross_income = 0
deduction = 0
net_pay = 0
HDMF = 100

# Imput of variables
company_name = str(input("Enter the company name: "))
employee_name = str(input("Enter the employee's name: "))
employee_number = str(input("Enter employee code: "))
employee_department = str(input("Enter employee's department: "))
pay_period_start = str(input("Enter the start date of pay period (mm/dd/yy): "))
pay_period_end = str(input("Enter the end date of pay period (mm/dd/yy): "))
rate_hour = float(input("Enter employee's rate per hour: "))
num_hrs_days = float(input("Enter employee's number of hours per payday: "))
num_hrs_ot = float(input("Enter employee's number of overtime in hours per payday: "))
num_hrs_absents = float(input("Enter employee's number of absences in hours per payday: "))
num_hrs_tardy = float(input("Enter employee's tardiness in hours per payday: "))
num_hrs_honor = float(input("Enter the amount of volunteer hours worked by the employee: "))

# Computing gross earnings
basic_pay = rate_hour * num_hrs_days
overtime_pay = rate_hour * num_hrs_ot
honorarium = rate_hour * num_hrs_honor

# Computing Gross Income
gross_income = basic_pay + overtime_pay + honorarium

# Computing value for deductions
tardiness = num_hrs_tardy * rate_hour
absences = num_hrs_absents * rate_hour

# Computing for SSS contribution
if gross_income >= 19750:
    sss_cont = 900
elif gross_income >= 19250:
    sss_cont = 877.50
elif gross_income >= 18750:
    sss_cont = 855.00
elif gross_income >= 18250:
    sss_cont = 832.50
elif gross_income >= 17750:
    sss_cont = 810
elif gross_income >= 17250:
    sss_cont = 787.50
elif gross_income >= 16750:
    sss_cont = 765
elif gross_income >= 16250:
    sss_cont = 742.50
elif gross_income >= 15750:
    sss_cont = 720
elif gross_income >= 15250:
    sss_cont = 697.50
elif gross_income >= 14750:
    sss_cont = 675
elif gross_income >= 14250:
    sss_cont = 652.50
elif gross_income >= 13750:
    sss_cont = 630
elif gross_income >= 13250:
    sss_cont = 607.50
elif gross_income >= 12750:
    sss_cont = 585
elif gross_income >= 12250:
    sss_cont = 562.50
elif gross_income >= 11750:
    sss_cont = 540
elif gross_income >= 11250:
    sss_cont = 517.50
elif gross_income >= 10750:
    sss_cont = 495
elif gross_income >= 10250:
    sss_cont = 472.50
elif gross_income >= 9750:
    sss_cont = 450
elif gross_income >= 9250:
    sss_cont = 427.50
elif gross_income >= 8750:
    sss_cont = 405
elif gross_income >= 8250:
    sss_cont = 382.50
elif gross_income >= 7750:
    sss_cont = 360
elif gross_income >= 7250:
    sss_cont = 337.50
elif gross_income >= 6750:
    sss_cont = 315
elif gross_income >= 6250:
    sss_cont = 292.50
elif gross_income >= 5750:
    sss_cont = 270
elif gross_income >= 5250:
    sss_cont = 247.50
elif gross_income >= 4750:
    sss_cont = 225
elif gross_income >= 4250:
    sss_cont = 202.50
else:
    sss_cont = 180

#Computing for Philhealth contribution
if gross_income >= 100000:
    phil_cont = 100000 * 0.05
elif gross_income >= 10000:
    phil_cont = gross_income * 0.05
else:
    phil_cont = 0

# Computing value for tax
if gross_income >= 333333:
    tax_cont = 91770.70 + ((gross_income - 333333) * 0.35)
elif gross_income >= 83333:
    tax_cont = 16770.70 + ((gross_income - 83333) * 0.30)
elif gross_income >= 33333:
    tax_cont = 4270.70 + ((gross_income - 33333) * 0.25)
elif gross_income >= 16667:
    tax_cont = 937.50 + ((gross_income - 16667) * 0.20)
elif gross_income >= 10417:
    tax_cont = (gross_income - 10417) * 0.15
else:
    tax_cont = 0

# Computing total deduction
deduction = absences + tardiness + tax_cont + sss_cont + phil_cont + HDMF

# Compute
net_pay = gross_income - deduction

print(f"Company: {company_name}")
print(f"Employee Name: {employee_name}")
print(f"Employee Code: {employee_number}")
print(f"Department: {employee_department}")
print(f"Salary cut-off: {pay_period_end}")
print(f"Pay period: {pay_period_start} to {pay_period_end}")
print(f"Basic pay: {basic_pay}")
print(f"Overtime: {overtime_pay}")
print(f"Honorarium: {honorarium}")
print(f"Absences: {absences}")
print(f"Tardiness: {tardiness}")
print(f"Withholding Tax: {tax_cont}")
print(f"SSS Contribution: {sss_cont}")
print(f"HDMF Contribution: {HDMF}")
print(f"Philhealth Contribution: {phil_cont}")
print(f"Deductions: {deduction}")
print(f"Gross Earnings: {gross_income}")
print(f"Net pay: {net_pay}")




