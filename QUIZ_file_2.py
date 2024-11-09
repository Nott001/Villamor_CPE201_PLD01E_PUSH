# main.py

from QUIZ_PLDL_VILLAMOR import CustomerInfo, BillingInfo

def display_bill(billing_info):
    total_amount_due = billing_info.calculate_total_current_amount()
    print("\n==================== Electric Bill ====================\n")
    print(f"Summary for Customer Account Number (CAN) {billing_info.customer_info.customer_account_num}\n")
    print(f"Customer Name :{billing_info.customer_info.customer_name}")
    print(f"Address       :{billing_info.customer_info.customer_street_add}, {billing_info.customer_info.customer_barangay}, {billing_info.customer_info.customer_city}\n")

    print(f"|  Previous Balance  |  ", end="")
    if billing_info.balance_prev_bill == 0:
        print("Thank you for your payment!")
    else:
        print(f"Please pay the amount of PHP {billing_info.balance_prev_bill:.2f}")

    print("\n|      Current Charges      |")
    print(f"|   Amount due: PHP {total_amount_due:.2f}   |   Due Date: {billing_info.due_date}   |")
    print("|    Total amount Due    |")
    print(f"|    PHP {total_amount_due:.2f}    |\n")

    print("\n|----------------------------------------------|")
    print("|                Service Info                  |")
    print("|----------------------------------------------|")
    print(f"|Service ID Number       : {billing_info.customer_info.customer_account_num}")
    print(f"|Rate                    : {billing_info.customer_rate}")
    print(f"|Contract In The Name of : {billing_info.customer_info.customer_name}")
    print(f"|Service Address         : {billing_info.customer_info.customer_street_add}, {billing_info.customer_info.customer_barangay}, {billing_info.customer_info.customer_city}\n")

    print("\n|----------------------------------------------|")
    print("|                Billing Info                  |")
    print("|----------------------------------------------|")
    print(f"| Bill Date               : {billing_info.bill_date}")
    print(f"| Meter Reading Date      : {billing_info.meter_reading_date}")
    print(f"| Billing Period          : {billing_info.billing_period}")
    print(f"| Due Date                : {billing_info.due_date}")
    print(f"| Total kWh               : {billing_info.actual_consumption}")
    print(f"| Total Current Amount    : {total_amount_due:.2f}")
    print(f"| Next Meter Reading      : {billing_info.next_meter_reading}")
    print("|----------------------------------------------|")

    print(f"\nTotal Amount Due: PHP {total_amount_due:.2f}")
    print("=======================================================")

def main():
    customer_info = CustomerInfo()
    billing_info = BillingInfo(customer_info)
    display_bill(billing_info)

if __name__ == "__main__":
    main()

