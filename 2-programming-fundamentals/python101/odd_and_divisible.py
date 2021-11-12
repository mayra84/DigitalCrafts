
num = int(input('Choose a number, any number: '))

def is_odd_and_three(num):
    if num % 3 == 0:
        if num % 2 == 1:
            print('Success!')
        else:
            print('Fail.')

is_odd_and_three(num)