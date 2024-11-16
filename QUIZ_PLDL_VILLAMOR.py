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




















