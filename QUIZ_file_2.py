import QUIZ_PLDL_VILLAMOR
customer = QUIZ_PLDL_VILLAMOR.CustomerInfo()
billing = QUIZ_PLDL_VILLAMOR.BillingInfo(customer)

def display_all_data():
    print("\n==================== Electric Bill ====================\n")
    print(f"Summary for Customer Account Number (CAN) {customer.customer_account_num}\n")
    print(f"Customer Name :{customer.customer_name}")
    print(
        f"Address       :{customer.customer_street_add}, {customer.customer_barangay}, {customer.customer_city}\n")

    print(f"|  Previous Balance  |  ", end="")
    if billing.balance_prev_bill == 0:
        print("Thank you for your payment!")
    else:
        print(f"Please pay the amount of PHP {billing.balance_prev_bill:.2f}")

    print("\n|      Current Charges      |")
    print(f"|   Amount due: PHP {billing.total_current_amount:.2f}   |   Due Date: {billing.due_date}   |")
    print("|    Total amount Due    |")
    print(f"|    PHP {billing.total_current_amount:.2f}    |\n")

    print("\n|----------------------------------------------|")
    print("|                Service Info                  |")
    print("|----------------------------------------------|")
    print(f"|Service ID Number       : {customer.customer_account_num}")
    print(f"|Rate                    : {billing.customer_rate}")
    print(f"|Contract In The Name of : {customer.customer_name}")
    print(
        f"|Service Address         : {customer.customer_street_add}, {customer.customer_barangay}, {customer.customer_city}\n")

    print("\n")
    print("|----------------------------------------------|")
    print("|                Billing Info                  |")
    print("|----------------------------------------------|")
    print(f"| Bill Date               : {billing.bill_date}")
    print(f"| Meter Reading Date      : {billing.meter_reading_date}")
    print(f"| Billing Period          : {billing.billing_period}")
    print(f"| Due Date                : {billing.due_date}")
    print(f"| Total kWh               : {billing.actual_consumption}")
    print(f"| Total Current Amount    : {billing.total_current_amount:.2f}")
    print(f"| Next Meter Reading      : {billing.next_meter_reading}")
    print("|----------------------------------------------|")

    print("\n|----------------------------------------------|")
    print("|                Your electric bill                 |")
    print("|----------------------------------------------|")
    print(f"|Bill Date               : {billing.bill_date}")
    print(f"|Bill Period             : {billing.billing_period}")
    print(f"|Meter Reading Date      : {billing.meter_reading_date}")
    print(f"|Next Meter Reading      : {billing.next_meter_reading}")
    print(f"|Customer Type           : {billing.customer_rate}")
    print(f"|Due date                : {billing.due_date}")
    print(f"|Rate this month         : {billing.rate_per_hour_res}")
    print(f"|Total kWh               : {billing.actual_consumption} kWh")
    print("\n")

    print("\n|----------------------------------------------|")
    print("|        Breakdown of Electricity Charges      |")
    print("|------------------------------------------------|")
    print("|                  Please pay                 |")
    print(f"Total Current Amount    : PHP {billing.total_current_amount:.2f}\n")
    print("|------------------------------------------------|")
    print(f"Generation Fee          : PHP {billing.generation:.2f}")
    print(f"Transmission Fee        : PHP {billing.transmission:.2f}")
    print(f"System Loss Fee         : PHP {billing.system_loss:.2f}")
    print(f"Distribution Fee        : PHP {billing.distribution:.2f}")
    print(f"Subsidies Fee           : PHP {billing.subsidies:.2f}")
    print(f"Government Taxes        : PHP {billing.government_taxes:.2f}")
    print(f"Universal Charges       : PHP {billing.universal_charges:.2f}")
    print(f"Renewable Fee           : PHP {billing.renewable:.2f}")
    print(f"Applied Credits         : PHP {billing.applied_credits:.2f}")
    print(f"Other Charges           : PHP {billing.other_charges:.2f}")
    print(f"Installment Due         : PHP {billing.installment_due:.2f}\n")
    print(f"Total Current Amount    : PHP {billing.total_current_amount:.2f}\n")
    print("=======================================================\n")
# Calling the function for display
display_all_data()



