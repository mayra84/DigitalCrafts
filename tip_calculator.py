def percentagePlus(bill_total, tip_percentage):
    if tip_percentage > 1:
        tip_percentage = tip_percentage / 100
    return bill_total + tip_percentage  * bill_total

bill_total = float(input('What is the total bill? '))
tip_percentage = float(input('What percentage would you like to tip? '))

total = percentagePlus(bill_total=bill_total, tip_percentage=tip_percentage)

print(f'Total bill is ${total}')
