deposited_amount = float(input("Enter the deposited amount: "))
term_ot_the_deposit = int(input("Enter term of the deposit in months: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
total_interest = deposited_amount * annual_interest_rate / 100
interest_per_month = total_interest / 12
total_amount = deposited_amount + (term_ot_the_deposit * interest_per_month)
print(total_amount)
