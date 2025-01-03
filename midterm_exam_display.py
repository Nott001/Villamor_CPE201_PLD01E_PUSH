# Import of classes from another file
import midterm_exam
customer_data = midterm_exam.Customerinfo()
billing_data = midterm_exam.Billing()
billing_data.billing_summary()

def display_all_data():
    # Displays data from service information to billing summary
    print("Advisory: Check payment WILL NOT BE ACCEPTED without \n the Statement of Account effective October 01, 2019")
    print("=" * 80)
    print("           |-          -|                 8390 DR A SANTOS AVE BF HOMES")
    print("           | -        - |                 PARANAQUE CITY")
    print("           |  -      -  |                 VAT Reg TIN 005-393-442-0000")
    print("           |   -    -   |                 SPM No.:")
    print("           |     -      |                 MAchine SN:")
    print("              MAYNILAD                     ")
    print("SOA # 00000000003456789012")
    print("\t\t\t\t\t\tSTATEMENT OF ACCOUNT\t\t\t\t\t\t")
    print("\t\t\t\t\tFor the Month of: February 2024\t\t\t\t\t\t")
    print("\n")
    print("\t\t\t\t\t\tSERVICE INFORMATION\t\t\t\t\t\t")
    print(f"Contract Account No  :{customer_data.contract_account_no}")
    print(f"Account Name         :{customer_data.customer_name}")
    print(f"Service Address      :{customer_data.service_address}")
    print(f"Rate Class           :{customer_data.rate_class}")
    print(f"Business Area        :{customer_data.business_area}")
    print("-" * 80)
    print("\t\t\t\t\t\tMETERING INFORMATION\t\t\t\t\t\t")
    print("Meter No.\t\t\t\t\t\tMRU No.\t\t\t\t\t\tSeq No.")
    print(f"{billing_data.meter_num}\t\t\t\t\t{billing_data.mru_num}\t\t\t\t\t{billing_data.seq_num}")
    print(f"Reading Date        :{billing_data.reading_date}")
    print(f"Present Reading     :{billing_data.present_reading}")
    print(f"Previous Reading    :{billing_data.previous_reading}")
    print(f"Consumption (cu.m)  :{billing_data.consumption}")
    print("\n")
    print(f"Previous {billing_data.consumption_period} Months \n Consumption")
    print("-" * 80)
    print("\t\t\t\t\t\tBILL & PAYMENT HISTORY\t\t\t\t\t\t")
    print("\n")
    print("Desct\t\t\tTotal Amountt\t\t\tOR#t\t\t\tDate")
    print("Description: WB-Water Bill, GD-Guarantee Deposit, MISC-Reopening Fee, Metering Charge")
    print("-" * 80)
    print("\t\t\t\t\t\tBILLING SUMMARY\t\t\t\t\t\t")
    print(f"BILLING PERIOD: {billing_data.billing_period_start} TO {billing_data.billing_period_end}")
    print(f"Current Charges                                        {billing_data.total_amount_due}")
    print(f"Basic Charge                                           {billing_data.basic_charge}")
    print(f"Environmental Charges (20% of Basic Charge)            {billing_data.environmental_charges}")
    print(f"Maintenance Service Charge (MSC)                       {billing_data.maintence_service_charge}")
    print(f"Total Current Charges Before Taxes                     {billing_data.total_charges_bef_tax}")
    print(f"Government Taxes                                       {billing_data.government_taxes}")
    print("\n")
    print("-" * 80)
    print(f"TOTAL AMOUNT DUE                                       {billing_data.total_amount_due}")
    print(f"PAYMENT DUE DATE                                       {billing_data.due_date}")
    print("=" * 80)
# Calling the function for displaying data
display_all_data()


