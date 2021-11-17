# Importing other functions from other files
from flip_coin import flip_coin
from roll_die import roll_die

# 
def menu():
    choice = input("""
Please choose an option:
1 - flip a coin
2 - roll a die
q - exit
:""")
    choice_options = ['1', '2', 'q']
    while choice not in choice_options:
        print('That is not a valid option. Please try again.')
        choice = menu()
    return choice 


def main():
    choice = menu()
    if choice == '1':
        flip_coin()
    elif choice == '2':
        roll_die()
    elif choice == 'q':
        exit()
    main()



main()