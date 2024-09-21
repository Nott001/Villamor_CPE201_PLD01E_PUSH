# Initializing values
basic_pay = 0
overtime_pay = 0
absences = 0
tardiness = 0
honorary=0
gross_income = 0
deduction = 0
net_pay = 0
HDMF = 100
company_name = ""
employee_name = ""
employee_department = ""
employee_number = 0


#Imput of variables
employee_name = str(input("Enter the employee's name: "))
employee_number = str(input("Enter employee number: "))
employee_department = str(input("Enter employee's department: "))
pay_period = str(input("Enter salary date cut-off: "))
rate_hour = float(input("Enter employee's rate per hour: "))
num_hrs_days = float(input("Enter employee's number of hours per day: "))
num_hrs_ot = float(input("Enter employee's number of overtime in hours per payday: "))
num_hrs_absents = float(input("Enter employee's number of absences in hours per payday: "))
honorarium = float(input("Enter the amount of volunteer hours worked by the employee: "))
tardiness = float(input("Enter employee's tardiness in hours per payday: "))

# Computing gross earnings
basic_pay = rate_hour * num_hrs_days
overtime_pay = rate_hour * num_hrs_ot
honorary = rate_hour * honorarium

# Computing Gross Income
gross_income = basic_pay + overtime_pay + honorary

# Computing value for deductions
if gross_income > 29750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 29250:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 28750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 28250:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 27750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 27250:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 26750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 26250:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 25750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 25250:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 24750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 24250:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 23750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 23250:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 22750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 22250:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 21750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 21250:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 19750:
    sss_cont = 900
    phil_cont = gross_income * 0.05
elif gross_income >= 19250:
    sss_cont = 877.50
    phil_cont = gross_income * 0.05
elif gross_income >= 18750:
    sss_cont = 855.00
    phil_cont = gross_income * 0.05
elif gross_income >= 18250:
    sss_cont = 832.50
    phil_cont = gross_income * 0.05
elif gross_income >= 17750:
    sss_cont = 810
    phil_cont = gross_income * 0.05
elif gross_income >= 17250:
    sss_cont = 787.50
    phil_cont = gross_income * 0.05
elif gross_income >= 16750:
    sss_cont = 765
    phil_cont = gross_income * 0.05
elif gross_income >= 16250:
    sss_cont = 742.50
    phil_cont = gross_income * 0.05
elif gross_income >= 15750:
    sss_cont = 720
    phil_cont = gross_income * 0.05
elif gross_income >= 15250:
    sss_cont = 697.50
    phil_cont = gross_income * 0.05
elif gross_income >= 14750:
    sss_cont = 675
    phil_cont = gross_income * 0.05
elif gross_income >= 14250:
    sss_cont = 652.50
    phil_cont = gross_income * 0.05
elif gross_income >= 13750:
    sss_cont = 630
    phil_cont = gross_income * 0.05
elif gross_income >= 13250:
    sss_cont = 607.50
    phil_cont = gross_income * 0.05
elif gross_income >= 12750:
    sss_cont = 585
    phil_cont = gross_income * 0.05
elif gross_income >= 12250:
    sss_cont = 562.50
    phil_cont = gross_income * 0.05
elif gross_income >= 11750:
    sss_cont = 540
    phil_cont = gross_income * 0.05
elif gross_income >= 11250:
    sss_cont = 517.50
    phil_cont = gross_income * 0.05
elif gross_income >= 10750:
    sss_cont = 495
    phil_cont = gross_income * 0.05
elif gross_income >= 10250:
    sss_cont = 472.50
    phil_cont = gross_income * 0.05
elif gross_income >= 9750:
    sss_cont = 450
    if 10000 <= gross_income <= 10250:
        phil_cont = gross_income * 0.05
    else:
        phil_cont = 0
elif gross_income >= 9250:
    sss_cont = 427.50
    phil_cont = 0
elif gross_income >= 8750:
    sss_cont = 405
    phil_cont = 0
elif gross_income >= 8250:
    sss_cont = 382.50
    phil_cont = 0
elif gross_income >= 7750:
    sss_cont = 360
    phil_cont = 0
elif gross_income >= 7250:
    sss_cont = 337.50
    phil_cont = 0
elif gross_income >= 6750:
    sss_cont = 315
    phil_cont = 0
elif gross_income >= 6250:
    sss_cont = 292.50
    phil_cont = 0
elif gross_income >= 5750:
    sss_cont = 270
    phil_cont = 0
elif gross_income >= 5250:
    sss_cont = 247.50
    phil_cont = 0
elif gross_income >= 4750:
    sss_cont = 225
    phil_cont = 0
elif gross_income >= 4250:
    sss_cont = 202.50
    phil_cont = 0
else:
    sss_cont = 180
    phil_cont = 0

# Computing value for tax
if gross_income >= 666667:
    tax_cont = 183541.80 + (gross_income * 0.35)
elif gross_income >= 166667:
    tax_cont = 33541.80 + (gross_income * 0.30)
elif gross_income >= 66667:
    tax_cont = 8541.80 + (gross_income * 0.25)
elif gross_income >= 33333:
    tax_cont = 1875 + (gross_income * 0.20)
elif gross_income >= 20833:
    tax_cont = gross_income * 0.15
else:
    tax_cont = 0

# Computing total deduction
deduction = absences + tardiness + tax_cont + sss_cont + phil_cont + HDMF

# Compute
net_pay = gross_income - deduction

print(f"Final pay: {net_pay}")











