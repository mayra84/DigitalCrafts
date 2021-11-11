def percentagePlus():
    bill_total = float(input('What is the total bill? '))
    tip_percentage = float(input('What percentage would you like to tip? '))
    if tip_percentage > 1:
        tip_percentage = tip_percentage / 100
    return bill_total + tip_percentage  * bill_total



# total = percentagePlus()

# print(f'Total bill is ${total}')


def tipCalculatorSplit():
    total = percentagePlus()
    num_people = float(input('How many people are in the group? '))

    return total / num_people


group_total = tipCalculatorSplit() 

print(f'Each person should pay ${round(group_total,2)}')
