from create import create
from delete import delete
from modify_view import modify_view
from view_lists_items import view_lists_items

def menu():
    choice = input("""
Please choose an option:
1 - Create a shopping list
2 - Modify or view shopping list
3 - Delete shopping list
4 - View all existing shopping lists and items
q - Quit
:
""")
    choice_options = ['1', '2', '3', '4', 'q']
    while choice not in choice_options:
        print('That is not a valid option. Please try again.')
        choice = menu()
    return choice

def main():
    choice = menu()
    if choice == '1':
        create()
    elif choice == '2':
        modify_view()
    elif choice == '3':
        delete()
    elif choice == '4':
        view_lists_items()
    elif choice == 'q':
        exit()
    main()

main()

