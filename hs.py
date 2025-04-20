def caculate_due_amount(total_bill, amount_paid):
    if amount_paid >= total_bill:
        print("No due amount. The customer has paid in full.")
        if amount_paid > total_bill:
            print(f"change to return: ${amount_paid - total_bill:.2f}")
            return 0.0
    else:
        due_amount = total_bill - amount_paid
        print(f"Due amount: ${due_amount:.2f}")
        return due_amount
print("Customer bill Payment")
total_bill = float(input("Enter the total bill amount: $"))
amount_paid = float(input("Enter the amount paid by the customer: $"))
caculate_due_amount(total_bill, amount_paid)