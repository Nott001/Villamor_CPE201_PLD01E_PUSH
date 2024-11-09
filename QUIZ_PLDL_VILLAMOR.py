class CustomerInfo:
    def __init__(self):
        self.customer_name = input("Enter customer name: ")
        self.customer_street_add = input("Enter customer address: ")
        self.customer_barangay = input("Enter customer barangay address: ")
        self.customer_city = input("Enter customer city address: ")
        self.customer_account_num = input("Enter customer account number: ")

class BillingInfo:
    def __init__(self, customer_info):
        self.customer_info = customer_info
        self.customer_rate = str(input("Enter whether residential or commercial: "))
        self.balance_prev_bill = float(input("Enter balance from previous billing: "))
        self.bill_date = input("Enter the billing date: ")
        self.meter_reading_date = input("Enter meter reading date: ")
        self.billing_period = input("Enter the billing period: ")
        self.due_date = input("Enter the due date: ")
        self.next_meter_reading = input("Enter the next meter reading date: ")
        self.actual_consumption = float(input("Enter the actual kilowatts/hr consumption: "))
        self.electrical_meter_num = input("Enter electrical meter number: ")
        self.rate_per_hour_res: float = 8.59
        self.rate_per_hour_com: float = 8.00
        self.current_consumption: float = 0.00
        self.total_current_amount = 0.00

        # Bill consumption summary
        self.generation = float(input("Enter generation fee: "))
        self.transmission = float(input("Enter transmission fee: "))
        self.system_loss = float(input("Enter system loss fee: "))
        self.distribution = float(input("Enter distribution fee: "))
        self.subsidies = float(input("Enter subsidy fee: "))
        self.government_taxes = float(input("Enter government taxes fee: "))
        self.universal_charges = float(input("Enter universal fee: "))
        self.renewable = float(input("Enter renewable fees: "))
        self.applied_credits = float(input("Enter applied fees: "))
        self.other_charges = float(input("Enter other fees: "))
        self.installment_due = float(input("Enter installment due: "))

    def total_current_amount(self):
        if self.customer_rate.lower() == "residential":
            self.current_consumption = self.actual_consumption * self.rate_per_hour_res
        elif self.customer_rate.lower() == "commercial":
            self.current_consumption = self.actual_consumption * self.rate_per_hour_com
        else:
            print("Invalid input in customer rate")
            return None
        self.total_current_amount = self.current_consumption + self.balance_prev_bill
        return self.total_current_amount

    def display_all_data(self):
        print("\n==================== Electric Bill ====================\n")
        print(f"Summary for Customer Account Number (CAN) {self.customer_info.customer_account_num}\n")
        print(f"Customer Name :{self.customer_info.customer_name}")
        print(f"Address       :{self.customer_info.customer_street_add}, {self.customer_info.customer_barangay}, {self.customer_info.customer_city}\n")

        print(f"|  Previous Balance  |  ", end="")
        if self.balance_prev_bill == 0:
            print("Thank you for your payment!")
        else:
            print(f"Please pay the amount of PHP {self.balance_prev_bill:.2f}")

        print("\n|      Current Charges      |")
        print(f"|   Amount due: PHP {self.total_current_amount:.2f}   |   Due Date: {self.due_date}   |")
        print("|    Total amount Due    |")
        print(f"|    PHP {self.total_current_amount:.2f}    |\n")

        print("\n|----------------------------------------------|")
        print("|                Service Info                  |")
        print("|----------------------------------------------|")
        print(f"|Service ID Number       : {self.customer_info.customer_account_num}")
        print(f"|Rate                    : {self.customer_rate}")
        print(f"|Contract In The Name of : {self.customer_info.customer_name}")
        print(f"|Service Address         : {self.customer_info.customer_street_add}, {self.customer_info.customer_barangay}, {self.customer_info.customer_city}\n")

        print("\n")
        print("|----------------------------------------------|")
        print("|                Billing Info                  |")
        print("|----------------------------------------------|")
        print(f"| Bill Date               : {self.bill_date}")
        print(f"| Meter Reading Date      : {self.meter_reading_date}")
        print(f"| Billing Period          : {self.billing_period}")
        print(f"| Due Date                : {self.due_date}")
        print(f"| Total kWh               : {self.actual_consumption}")
        print(f"| Total Current Amount    : {self.total_current_amount:.2f}")
        print(f"| Next Meter Reading      : {self.next_meter_reading}")
        print("|----------------------------------------------|")

        print("\n|----------------------------------------------|")
        print("|                Your electric bill                 |")
        print("|----------------------------------------------|")
        print(f"|Bill Date               : {self.bill_date}")
        print(f"|Bill Period             : {self.billing_period}")
        print(f"|Meter Reading Date      : {self.meter_reading_date}")
        print(f"|Next Meter Reading      : {self.next_meter_reading}")
        print(f"|Customer Type           : {self.customer_info}")
        print(f"|Due date                : {self.due_date}")
        print(f"|Rate this month         : {self.rate_per_hour_res}")
        print(f"|Total kWh               : {self.actual_consumption} kWh")
        print("\n")

        print("\n|----------------------------------------------|")
        print("|        Breakdown of Electricity Charges      |")
        print("|------------------------------------------------|")
        print("|                  Please pay                 |")
        print(f"Total Current Amount    : PHP {self.total_current_amount:.2f}\n")
        print("|------------------------------------------------|")
        print(f"Generation Fee          : PHP {self.generation:.2f}")
        print(f"Transmission Fee        : PHP {self.transmission:.2f}")
        print(f"System Loss Fee         : PHP {self.system_loss:.2f}")
        print(f"Distribution Fee        : PHP {self.distribution:.2f}")
        print(f"Subsidies Fee           : PHP {self.subsidies:.2f}")
        print(f"Government Taxes        : PHP {self.government_taxes:.2f}")
        print(f"Universal Charges       : PHP {self.universal_charges:.2f}")
        print(f"Renewable Fee           : PHP {self.renewable:.2f}")
        print(f"Applied Credits         : PHP {self.applied_credits:.2f}")
        print(f"Other Charges           : PHP {self.other_charges:.2f}")
        print(f"Installment Due         : PHP {self.installment_due:.2f}\n")
        print(f"Total Current Amount    : PHP {self.total_current_amount:.2f}\n")
        print("=======================================================\n")

#calling of functions
customer_info = CustomerInfo()
billing_info = BillingInfo(customer_info)
billing_info.display_all_data()

















