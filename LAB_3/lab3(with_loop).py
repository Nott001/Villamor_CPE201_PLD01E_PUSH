# Initializing values
gross_income = 0
deduction = 0
net_pay = 0
HDMF = 100

# Input of variables
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
thresholds = [19750, 19250, 18750, 18250, 17750, 17250, 16750, 16250, 15750, 15250, 14750, 14250, 13750, 13250, 12750,
              12250, 11750, 11250, 10750, 10250, 9750, 9250, 8750, 8250, 7750, 7250, 6750, 6250, 5750, 5250, 4750, 4250]
contributions = [900, 877.50, 855, 832.50, 810, 787.50, 765, 742.50, 720, 697.50, 675, 652.50, 630, 607.50, 585, 562.50,
                 540, 517.50, 495, 472.50, 450, 427.50, 405, 382.50, 360, 337.50, 315, 292.50, 270, 247.50, 225, 202.50]

for threshold, contribution in zip(thresholds, contributions):
    if gross_income >= threshold:
        sss_cont = contribution
        break
else:
    sss_cont = 0

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

